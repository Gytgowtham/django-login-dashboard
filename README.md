# 🔐 Django Login Dashboard

A professional full-stack web application built with **Django** featuring user authentication and a modern Bootstrap dashboard UI.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat&logo=bootstrap)

---

## ✨ Features

- User Login & Logout (Django Auth)
- Protected Dashboard (Login Required)
- Professional Dark Green UI with Bootstrap 5
- Responsive Sidebar Navigation
- Stats Cards & Activity Feed

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python 3.13 | Backend Language |
| Django 6.0 | Web Framework |
| Bootstrap 5.3 | Frontend UI |
| SQLite | Database |
| HTML/CSS | Templates |

---

## 🚀 Setup & Run Locally
```bash
# 1. Clone the repo
git clone https://github.com/Gytgowtham/django-login-dashboard.git
cd django-login-dashboard

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 📁 Project Structure
```
django-login-dashboard/
├── userloginproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── templates/
│   ├── registration/
│   │   └── login.html
│   └── users/
│       ├── base.html
│       └── dashboard.html
├── manage.py
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author
<img width="1920" height="1080" alt="Screenshot 2026-03-30 171933" src="https://github.com/user-attachments/assets/4ec033aa-2e55-40eb-bced-b72b91db958d" />
<img width="1920" height="1080" alt="Screenshot 2026-03-30 170018" src="https://github.com/user-attachments/assets/f4a38cc9-48b3-461f-b2f4-d64c8417e98e" />


**Gowtham Krishnan**  
[![GitHub](https://img.shields.io/badge/GitHub-Gytgowtham-black?style=flat&logo=github)](https://github.com/Gytgowtham)
