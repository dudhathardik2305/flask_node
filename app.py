from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm #, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from functools import wraps
from models.models import db, ContactMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# app.config['RECAPTCHA_PUBLIC_KEY'] = 'your_site_key'
# app.config['RECAPTCHA_PRIVATE_KEY'] = 'your_secret_key'

class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
    submit = SubmitField('Login')


class SignUp(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
    submit = SubmitField('SignUp')

class Contact(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = PasswordField('Email', validators=[DataRequired()])
    message = PasswordField('message', validators=[DataRequired()])
    # recaptcha = RecaptchaField()
    submit = SubmitField('SignUp')


@app.route('/')
def home():
    return render_template('landing.html', form=LoginForm())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignUp()
	if form.validate_on_submit():
		return redirect(url_for('dashboard'))
	return render_template('signup.html', form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/thank-you')
def thankyou():
    return render_template('thank-you.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
    	return redirect(url_for('thankyou'))
    return render_template('contact.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        # save or send email
        pass
    return render_template('base.html')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('logout'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)

