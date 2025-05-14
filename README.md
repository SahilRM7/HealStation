# ❤️ Healthcare Backend – Patient and Doctor Management System
Healthcare Backend is a RESTful backend system designed for managing patient and doctor records, including patient-doctor mappings. Built using Django, Django REST Framework (DRF), and PostgreSQL, it supports secure user registration, authentication, and data management through JWT tokens.
---

## 🧠 Project Objective
- To streamline healthcare data management by:
- Providing secure user authentication via JWT tokens
- Allowing registered users to manage patients and doctors
- Enabling efficient patient-doctor mappings
- Ensuring data integrity and secure storage using PostgreSQL
---

## 🔍 Features
- 🔐 User Authentication: Secure login and registration using JWT
- 📝 Patient Management: Add, update, view, and delete patient records
- 👨‍⚕️ Doctor Management: Add, update, view, and delete doctor profiles
- 🔗 Patient-Doctor Mapping: Assign doctors to patients and manage associations
- 📊 Data Validation and Error Handling: Comprehensive validation and meaningful error responses
- 💾 Database Security: Uses environment variables to secure sensitive data

## 🚀 Installation Guide

To run this project locally, follow these steps:

### 1. Clone the Repository
    git clone https://github.com/SahilRM7/HealStation.git
### 2. Navigate to the project directory: cd HealStation
### 3. (Optional) Create and activate a virtual environment: python3 -m venv venv and source venv/bin/activate
### 4. Install the required dependencies: pip install -r requirements.txt
### 5. Set up the database by running migrations: python manage.py migrate
### 6. Create a superuser for accessing the admin panel: python manage.py createsuperuser
### 7. Start the development server: python manage.py runserver
### 8. Open a web browser and access the application at http://localhost:8000
