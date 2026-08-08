🏥 HospitalQueueAI
An AI-powered hospital appointment and queue management system built with Flask and Google Gemini AI.

HospitalQueueAI is a web-based application designed to simplify the hospital appointment and patient queue management process.

The application allows patients to register their details, enter symptoms, receive a suggested medical department, book an appointment, receive a queue token, check their queue status, and interact with an AI-powered chatbot.

📌 Project Overview
In traditional hospital systems, patients may need to wait for long periods and manually communicate their symptoms and appointment requirements.

HospitalQueueAI provides a simple digital solution where patients can:

Register their details
Enter their symptoms
Get a suggested doctor/department
Book an appointment
Receive a queue token
Check their queue position
View estimated waiting time
Interact with an AI chatbot
The project combines a Flask backend, HTML/CSS/JavaScript frontend, and Google Gemini AI.

✨ Features
👤 1. Patient Registration
Patients can register by providing:

Patient name
Age
Phone number
Symptoms
The application validates the information and processes the patient's symptoms.

🩺 2. Doctor / Department Recommendation
The system analyzes the patient's age and symptoms and suggests an appropriate department.

Example recommendations
Symptoms	Suggested Department
Fever, cold, cough	General Physician
Chest or heart symptoms	Cardiologist
Headache or brain-related symptoms	Neurologist
Skin or allergy symptoms	Dermatologist
Eye-related symptoms	Ophthalmologist
Bone or joint symptoms	Orthopedic
Age below 16	Pediatrician
This feature helps patients identify the appropriate hospital department before booking an appointment.

🤖 3. AI-Powered Chatbot
HospitalQueueAI includes an AI chatbot powered by Google Gemini.

Patients can enter their symptoms and receive general informational guidance.

Example
Patient:
I have fever and cough.

AI:
General Physician may be an appropriate department.
Please consult a qualified healthcare professional for medical advice.

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

Follow these steps to run HospitalQueueAI locally.

1. Clone the Repository
git clone https://github.com/pojjuruhepsiba/HospitalQueueAI.git

Navigate to the project directory:

cd HospitalQueueAI
2. Create a Virtual Environment
python -m venv venv
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
3. Install Dependencies
pip install flask python-dotenv google-generativeai
4. Configure Gemini API Key

HospitalQueueAI uses Google Gemini AI for the chatbot.

Create a .env file in the project root:

HospitalQueueAI/
│
├── .env
├── app.py
├── README.md
└── ...

Add your Gemini API key:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

The application loads the API key using environment variables:

import os
from dotenv import load_dotenv

load_dotenv()

Gemini is configured using:

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
🔒 Security

The .env file is excluded from Git using .gitignore:

.env

Never upload your .env file or API key to GitHub.

5. Run the Application

Start the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000
🔄 Application Workflow
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
             │   Recommendation │
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

Provides access to the main HospitalQueueAI features.

Users can navigate to:

Registration
Appointment Booking
Queue Management
AI Chatbot
📝 Registration Page

Patients enter:

Name
Age
Phone Number
Symptoms
🩺 Appointment Page

Displays the recommended doctor or department and allows the patient to book an appointment.

🎫 Queue Page

Displays:

Queue Token
Patient Name
Department / Doctor
Patients Ahead
Estimated Waiting Time
🤖 Chatbot Page

Allows users to enter symptoms and receive AI-generated general information using Google Gemini AI.

✅ Success Page

Displays the appointment confirmation and generated queue token.

📸 Screenshots
📝 Patient Registration

🏥 Hospital Features

📋 Hospital Form

📅 Book Appointment

🎫 Queue Management

🤖 AI Chatbot

🧠 AI Checker

🧪 Testing

The following features can be tested manually.

Patient Registration
Enter patient name.
Enter age.
Enter phone number.
Enter symptoms.
Submit the registration form.
Doctor Recommendation

Test symptoms such as:

Fever
Cold
Cough
Chest pain
Headache
Skin allergy
Eye problem
Joint pain
Appointment Booking
Complete patient registration.
Check the recommended department.
Book the appointment.
Verify the generated queue token.
Queue Management
Open the queue page.
Verify the patient token.
Check the number of patients ahead.
Check the estimated waiting time.
AI Chatbot
Open the chatbot.
Enter a symptom.
Submit the question.
Verify the AI response.
🎫 Example Queue
-----------------------------------------
             HOSPITAL QUEUE
-----------------------------------------

Token       Patient        Department

HSP-001     Patient 1      General Physician
HSP-002     Patient 2      Cardiologist
HSP-003     Patient 3      Neurologist

-----------------------------------------


HospitalQueueAI is an educational and academic project.

The AI chatbot and department recommendation features provide general informational guidance only.

They are not intended to provide medical diagnosis, emergency treatment, or professional medical advice.

Patients should consult qualified healthcare professionals for medical concerns.

🚀 Future Enhancements
🗄️ MySQL or MongoDB database integration
👨‍⚕️ Doctor login and dashboard
👤 Patient login and profile
📊 Admin dashboard
📅 Real-time appointment scheduling
🔔 Email and SMS notifications
📈 Hospital analytics
🤖 Multilingual AI chatbot
🎙️ Voice-based chatbot
☁️ Cloud deployment
📈 Project Benefits

HospitalQueueAI provides a simple digital solution for hospital appointment and queue management.

Benefits
⏱️ Reduced waiting confusion
🎫 Digital queue tokens
🩺 Department recommendation
🤖 AI-powered assistance
📅 Easy appointment booking
📱 User-friendly interface
🔐 Environment-based API security
🎓 Academic Project

This project demonstrates:

Python programming
Flask web development
HTML/CSS/JavaScript
REST-style web routes
AI API integration
Environment variable management
Git and GitHub
Hospital appointment workflow
Queue management

👨‍💻 Author
Pojjuru Hepsiba
GitHub

https://github.com/pojjuruhepsiba

Project Repository

HospitalQueueAI

📄 License

This project is created for educational and academic purposes.

You are free to study and modify the source code for learning purposes.

⭐ Support

If you find this project useful, please consider giving the repository a ⭐ on GitHub.