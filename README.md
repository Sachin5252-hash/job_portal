# 💼 Job Portal 

A web-based **Job Portal application** built with **Python and Django**.  
The platform allows users to explore job opportunities and provides functionality for managing job listings.

## 🚀 Features

- 👤 User registration and login
- 🔐 User authentication
- 💼 Browse available jobs
- 🔎 Search and filter jobs
- 📄 View detailed job information
- 🏢 Company and job management
- 📝 Apply for jobs
- 📊 Manage job applications
- 🛠️ Django Admin panel
- 🗄️ Database integration

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML5**
- **CSS3**
- **JavaScript**
- **SQLite** / Database
- **Git & GitHub**

## 📁 Project Structure

```text
job_portal/
│
├── manage.py
├── job_portal/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── jobs/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── ...
│
├── templates/
├── static/
├── db.sqlite3
└── README.md
```

> The exact folder structure may vary depending on your project configuration.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sachin5252-hash/job_portal.git
```

### 2. Go to the project directory

```bash
cd job_portal
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

If your project has a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you don't have one yet:

```bash
pip install django
```

## 🗄️ Database Setup

Run migrations:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

## 👨‍💻 Create Admin User

To access the Django Admin panel:

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal.

## ▶️ Run the Project

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

For the Django Admin panel:

```text
http://127.0.0.1:8000/admin/
```

## 🔑 Environment Variables

If your project uses sensitive information such as database passwords, secret keys, or API keys, store them in a `.env` file.

Example:

```text
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=your-database-url
```

Do **not** upload `.env` files or passwords to GitHub.

## 📌 Future Improvements

- Resume upload
- Advanced job search
- Job recommendations
- Email notifications
- Company profiles
- Application tracking
- REST API
- PostgreSQL integration
- Deployment to a cloud platform

## 👨‍💻 Author

**Sachin Parashar**

GitHub:  
https://github.com/Sachin5252-hash

## 📄 License

This project is created for learning and development purposes.
