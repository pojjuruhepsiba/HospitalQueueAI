# 🏥 HospitalQueueAI

> An AI-powered hospital appointment and queue management system built with Flask and Google Gemini AI.

HospitalQueueAI is a web-based application designed to simplify the hospital appointment and patient queue management process.

The application allows patients to register their details, enter symptoms, receive a suggested medical department, book an appointment, receive a queue token, check their queue status, and interact with an AI-powered chatbot.

---

## 📌 Project Overview

In traditional hospital systems, patients may need to wait for long periods and manually communicate their symptoms and appointment requirements.

HospitalQueueAI provides a simple digital solution where patients can:

- Register their details
- Enter their symptoms
- Get a suggested doctor/department
- Book an appointment
- Receive a queue token
- Check their queue position
- View estimated waiting time
- Interact with an AI chatbot

The project combines a **Flask backend**, **HTML/CSS/JavaScript frontend**, and **Google Gemini AI**.

---

# ✨ Features

## 👤 1. Patient Registration

Patients can register by providing:

- Patient name
- Age
- Phone number
- Symptoms

The application validates the information and processes the patient's symptoms.

---

## 🩺 2. Doctor / Department Recommendation

The system analyzes the patient's age and symptoms and suggests an appropriate department.

### Example recommendations

| Symptoms | Suggested Department |
|---|---|
| Fever, cold, cough | General Physician |
| Chest or heart symptoms | Cardiologist |
| Headache or brain-related symptoms | Neurologist |
| Skin or allergy symptoms | Dermatologist |
| Eye-related symptoms | Ophthalmologist |
| Bone or joint symptoms | Orthopedic |
| Age below 16 | Pediatrician |

This feature helps patients identify the appropriate hospital department before booking an appointment.

---

# 🤖 3. AI-Powered Chatbot

HospitalQueueAI includes an AI chatbot powered by **Google Gemini**.

Patients can enter their symptoms and receive general informational guidance.

### Example

```text
Patient:
I have fever and cough.

AI:
General Physician may be an appropriate department.
Please consult a qualified healthcare professional for medical advice.

```
📅 4. Appointment Booking

Patients can book an appointment after registration.

The system stores the appointment information and generates a unique queue token.

Example
HSP-001
HSP-002
HSP-003

Each patient receives a token after successful booking.

🎫 5. Queue Management

The queue management system provides information about the patient's position in the queue.

It displays:

Patient name
Queue token
Doctor/department
Number of patients ahead
Estimated waiting time

The estimated waiting time is calculated based on the number of patients ahead.

⏱️ 6. Waiting Time Estimation

The application estimates the waiting time using the queue position.

For example:

Patient 1 → 0 minutes
Patient 2 → 5 minutes
Patient 3 → 10 minutes
Patient 4 → 15 minutes

This helps patients understand their approximate waiting time.

🌐 7. Responsive Web Interface

The application provides a clean and user-friendly web interface using:

HTML5
CSS3
JavaScript

The interface is designed to work across different screen sizes.

🛠️ Technologies Used
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Flask
Artificial Intelligence
Google Gemini AI
Google Generative AI API
Environment Management
Python-dotenv
.env environment variables
Version Control
Git
GitHub
📂 Project Structure
HospitalQueueAI/
│
├── Screenshots/
│   ├── ai checker.png
│   ├── book-appoinment.png
│   ├── chatbot.png
│   ├── checks-queue.png
│   ├── hospital-features.png
│   ├── hospital-form.png
│   └── registration.png
│
├── static/
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── appointment.html
│   ├── chatbot.html
│   ├── index.html
│   ├── queue.html
│   ├── register.html
│   └── success.html
│
├── .gitignore
├── app.py
└── README.md
⚙️ Installation and Setup

Follow the steps below to run HospitalQueueAI locally.

Step 1: Clone the Repository
git clone https://github.com/pojjuruhepsiba/HospitalQueueAI.git

Navigate into the project directory:

cd HospitalQueueAI
Step 2: Create a Virtual Environment

Create a Python virtual environment:

python -m venv venv
Windows

Activate the virtual environment:

venv\Scripts\activate
macOS / Linux
source venv/bin/activate
Step 3: Install Dependencies

Install the required Python packages:

pip install flask python-dotenv google-generativeai
🔐 Step 4: Configure Gemini API Key

HospitalQueueAI uses Google Gemini AI.

Create a file named:

.env

in the root project directory.

Your project should look like:

HospitalQueueAI/
│
├── .env
├── app.py
├── README.md
└── ...

Add your Gemini API key:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY
🔒 API Key Security

Never directly write your API key inside app.py.

The application uses:

import os
from dotenv import load_dotenv

load_dotenv()

and:

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

The .env file is ignored by Git using .gitignore.

The .gitignore file contains:

.env

Therefore, your API key should remain private.

⚠️ Never upload your .env file to GitHub.

▶️ Step 5: Run the Application

Start the Flask application:

python app.py

The Flask development server should start.

You should see something similar to:

Running on http://127.0.0.1:5000

Open your browser and visit:

http://127.0.0.1:5000
🔄 Application Workflow

The application follows this workflow:

                 ┌──────────────────┐
                 │      Patient     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   Registration   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Enter Symptoms   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Doctor/Department│
                 │   Suggestion     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Book Appointment │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Generate Token   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │  Queue Tracking  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   AI Chatbot     │
                 └──────────────────┘
📄 Application Pages
🏠 Home Page

The home page provides access to the main HospitalQueueAI features.

Users can navigate to registration, appointments, queue management, and chatbot services.

📝 Registration Page

The registration page collects:

Name
Age
Phone Number
Symptoms

After submitting the form, the system analyzes the patient's information.

🩺 Appointment Page

The appointment page displays the suggested department/doctor.

The patient can proceed with the appointment booking.

🎫 Queue Page

The queue page displays patient queue information.

It includes:

Token
Patient Name
Department / Doctor
Patients Ahead
Waiting Time
🤖 Chatbot Page

The chatbot allows users to enter symptoms and receive AI-generated general information.

The chatbot uses the Google Gemini API.

✅ Success Page

After successfully booking an appointment, the application displays:

Appointment Successfully Booked

Patient Name
Doctor / Department
Queue Token
📸 Screenshots
📝 Patient Registration

🏥 Hospital Features

📋 Hospital Form

📅 Book Appointment

🎫 Queue Management

🤖 AI Chatbot

🧠 AI Checker

🔗 Project Repository

GitHub Repository:

https://github.com/pojjuruhepsiba/HospitalQueueAI

🧪 Testing

The following application features can be tested manually:

Patient Registration
Enter patient name
Enter age
Enter phone number
Enter symptoms
Submit registration
Doctor Recommendation

Test different symptoms:

Fever
Cold
Cough
Chest pain
Headache
Skin allergy
Eye problem
Joint pain
Appointment
Select/confirm the recommended department
Book appointment
Verify the generated token
Queue
Open the queue page
Verify patient token
Verify patients ahead
Verify estimated waiting time
AI Chatbot
Enter a symptom
Submit the question
Verify the AI response
📌 Example Queue

Example:

-----------------------------------------
          HOSPITAL QUEUE
-----------------------------------------

Token       Patient        Department
HSP-001     Patient 1      General Physician
HSP-002     Patient 2      Cardiologist
HSP-003     Patient 3      Neurologist

-----------------------------------------
🔐 Security Features

HospitalQueueAI follows basic security practices:

API keys are stored using environment variables.
.env is excluded from Git.
Sensitive credentials are not included in source code.
.gitignore prevents accidental upload of environment files.
⚠️ Medical Disclaimer

HospitalQueueAI is an educational and academic project.

The AI chatbot and doctor/department recommendation features provide general informational guidance only.

They are not intended to provide medical diagnosis, emergency treatment, or professional medical advice.

Patients should consult qualified healthcare professionals for medical concerns.

In an emergency, contact appropriate local emergency medical services.

🚀 Future Enhancements

The following features can be added in future versions:

🗄️ Database
MySQL integration
MongoDB integration
Persistent patient records
Appointment history
👨‍⚕️ Doctor Management
Doctor login
Doctor dashboard
Doctor availability
Department management
👤 Patient Management
Patient login
Patient profile
Appointment history
Medical record management
📊 Admin Dashboard
Total patients
Total appointments
Active queue
Doctor statistics
Department statistics
Daily appointment analytics
🔔 Notifications
Email notifications
SMS notifications
Appointment reminders
Queue status notifications
🤖 AI Improvements
Improved symptom classification
Multilingual chatbot
Voice-based chatbot
More detailed department recommendations
☁️ Deployment

The application can be deployed using cloud platforms such as:

Render
Railway
PythonAnywhere
Google Cloud
AWS
📈 Project Benefits

HospitalQueueAI helps reduce manual hospital queue management and provides a simple digital experience for patients.

Benefits include:
⏱️ Reduced waiting confusion
🎫 Digital queue tokens
🩺 Department recommendation
🤖 AI-powered assistance
📅 Easy appointment booking
📱 User-friendly interface
🔐 Environment-based API security
🎓 Academic Project

This project was developed as an educational project to demonstrate:

Python programming
Flask web development
HTML/CSS/JavaScript
REST-style web routes
AI API integration
Environment variable management
Git and GitHub
Basic hospital workflow automation
👨‍💻 Author
Pojjuru Hepsiba

GitHub:

https://github.com/pojjuruhepsiba

Project:

https://github.com/pojjuruhepsiba/HospitalQueueAI

📄 License

This project is created for educational and academic purposes.

You are free to study and modify the source code for learning purposes.

⭐ Support

If you find this project useful, you can give the repository a ⭐ on GitHub.
