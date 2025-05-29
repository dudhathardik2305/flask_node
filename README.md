# 🏗️ Villa Construction Portal

A modern Flask-based web portal for video sharing, contact messaging, and secure user authentication with reCAPTCHA protection.

---

## 🌐 Features

- 🔐 Login & Signup (with reCAPTCHA)
- 📨 Contact form with DB storage and email notifications
- 📍 Embedded Google Map
- 🎥 Embedded video sections
- 📁 Modern UI with custom CSS

---

## 🏠 Home

![Home Page](static/images/screenshots/home.png)

---

## ℹ️ About Us

![About Us](static/images/screenshots/about.png)

---

## 📬 Contact Us

![Contact Us](static/images/screenshots/contact.png)

---

## 🔑 Login

![Login](static/images/screenshots/login.png)

---

## 🆕 SignUp

![SignUp](static/images/screenshots/signup.png)

---

## ⚙️ Tech Stack

- **Flask** (backend)
- **Flask-WTF** (form handling with reCAPTCHA)
- **Flask-SQLAlchemy** (ORM)
- **WTForms** (form validation)
- **SQLite** (database)
- **HTML/CSS/JS** (frontend)

---

## 🚀 How to Run

```bash
# Clone this repository
git clone https://github.com/yourusername/villa-portal.git
cd villa-portal

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```