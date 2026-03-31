from fastapi import FastAPI
from twilio.rest import Client

app = FastAPI()

# Twilio Credentials (replace with your actual values)
TWILIO_SID = ""
TWILIO_TOKEN = ""
TWILIO_PHONE = "+12"  # Twilio number
YOUR_REAL_PHONE = "+923"  # Your phone

@app.post("/add-patient/")
def add_patient(name: str, age: int):
    # 1️⃣ Simulate adding patient to DB
    # (Replace with your actual DB code)
    print(f"Adding patient: {name}, Age: {age}")

    # 2️⃣ Send SMS via Twilio
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        message = client.messages.create(
            body=f"🚨 Hive Alert: New Patient Registered! Name: {name}, Age: {age}",
            from_=TWILIO_PHONE,
            to=YOUR_REAL_PHONE
        )
        sms_status = "SMS Sent Successfully!"
    except Exception as e:
        sms_status = f"SMS Failed: {e}"

    # 3️⃣ Return response
    return {"message": "Patient added to database", "sms_status": sms_status}