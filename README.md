# 🚀 FastAPI Patient Notification API (Twilio Integration)

## 📌 Overview

A production-ready **FastAPI backend system** that integrates with **Twilio API** to send real-time SMS notifications whenever a new patient is registered.

This project demonstrates:

* Event-driven architecture
* Third-party API integration
* Scalable backend design for SaaS applications

---

## ⚙️ Key Features

* ⚡ High-performance FastAPI backend
* 📩 Real-time SMS notifications using Twilio
* 🔐 Environment-based secure configuration
* 🧱 Modular and scalable project structure
* 🧠 Intelligent error handling (API limits, failures)
* 📊 Logging for monitoring and debugging

---

## 🏗️ Tech Stack

* 🐍 Python
* ⚡ FastAPI
* 📡 Twilio API
* 🚀 Uvicorn
* 🔐 Python-dotenv

---

## 📁 Project Structure

```
fastapi-twilio-patient-api/
│
├── app/
│   ├── main.py              # API entry point
│   ├── models.py            # Pydantic models
│   ├── services/
│   │   └── sms_service.py   # Twilio integration logic
│   ├── core/
│   │   └── config.py        # Environment configuration
│   └── utils/
│       └── logger.py        # Logging setup
│
├── .env.example             # Environment variables template
├── requirements.txt         # Project dependencies
├── README.md                # Documentation
└── .gitignore               # Ignored files
```

---

## 🔑 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-twilio-patient-api.git
cd fastapi-twilio-patient-api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
TWILIO_SID=your_account_sid
TWILIO_TOKEN=your_auth_token
TWILIO_PHONE=+1234567890
YOUR_REAL_PHONE=+923000000000
```

---

## ▶️ Run the Application

```bash
python -m uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### ➤ POST `/add-patient/`

#### Request Body

```json
{
  "name": "Ali",
  "age": 45
}
```

#### Response

```json
{
  "message": "Patient added to database",
  "sms_status": "SMS Sent Successfully!",
  "patient": {
    "name": "Ali",
    "age": 45
  }
}
```

---

## ⚠️ Twilio Trial Limitations

* ❌ Maximum 5 SMS per day
* ❌ Only verified numbers allowed
* ⚠️ Trial message branding included

---

## 🚀 Future Enhancements

* 🗄️ PostgreSQL / MySQL database integration
* 🔁 Background tasks (Celery / Redis)
* 📧 Email notifications (SendGrid API)
* 💬 WhatsApp API integration
* ☁️ Cloud deployment (Render / AWS / Railway)

---

## 💼 Real-World Use Cases

* 🏥 Hospital Management Systems
* 📅 Appointment Reminder Systems
* 📊 CRM Automation Workflows
* ⚙️ Event-Driven SaaS Platforms

---

## 👨‍💻 Author

**Wajiha**
📍 Remote Backend Developer | FastAPI Specialist

---

