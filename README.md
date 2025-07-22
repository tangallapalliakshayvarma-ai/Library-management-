# 📚 Library Management System (Django Project)

A simple and elegant web app built with Django to manage books in a library. You can:
- ➕ Add books
- 🔍 Search for books by title or author
- 📖 View all saved books
- ⚙️ (Coming Soon) Manage users

---

## 🚀 Features

- Clean and user-friendly interface
- Book addition form with title, author, and ISBN
- Real-time search by keyword
- SQLite database-backed
- Django templating with minimal CSS

---

## 🛠️ Tech Stack

- Python 3.7+
- Django
- HTML/CSS
- SQLite (default)

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/tangallapalliakshayvarma-ai/Library-management-.git
cd Library-management-

2. Create Virtual Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate  

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Run the Django Development Server

python manage.py runserver

Visit in Browser

Once the server is running, open your browser and go to:

http://127.0.0.1:8000/