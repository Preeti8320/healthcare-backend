# Healthcare Management API (Django REST Framework)

A robust backend REST API built with **Django REST Framework (DRF)**, **PostgreSQL**, and **JWT Authentication (simplejwt)** for managing patient records, doctor profiles, and patient-doctor mappings.

---

## 🚀 Features

- **User Authentication:** Secure registration and login using JWT (`access` and `refresh` tokens).
- **Doctor Management:** Full CRUD operations to manage doctor profiles.
- **Patient Management:** Full CRUD operations to manage patient records.
- **Patient-Doctor Mapping:** Map patients to specific assigned doctors.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** `djangorestframework-simplejwt`
- **Testing Tools:** Postman

---

## 📌 API Endpoints Summary

| Feature | Method | Endpoint | Auth Required |
| :--- | :--- | :--- | :--- |
| **Register** | `POST` | `/api/auth/register/` | ❌ No |
| **Login** | `POST` | `/api/auth/login/` | ❌ No |
| **List/Create Doctors** | `GET` / `POST` | `/api/doctors/` | 🔒 Yes (Bearer Token) |
| **Doctor Detail** | `GET` / `PUT` / `DELETE` | `/api/doctors/<id>/` | 🔒 Yes (Bearer Token) |
| **List/Create Patients** | `GET` / `POST` | `/api/patients/` | 🔒 Yes (Bearer Token) |
| **Patient Detail** | `GET` / `PUT` / `DELETE` | `/api/patients/<id>/` | 🔒 Yes (Bearer Token) |
| **Create Mapping** | `POST` | `/api/mappings/` | 🔒 Yes (Bearer Token) |

---

## ⚙️ Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jagriti2005/](https://github.com/jagriti2005/)<your-repo-name>.git
   cd <your-repo-name>