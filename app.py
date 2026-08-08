
from flask import Flask, render_template, request,jsonify

import os

from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

appointments = []

appointments = []

def suggest_doctor(age, symptom):

    symptom = symptom.lower()

    if age <= 15:
        return "Pediatrician"

    if "fever" in symptom or "cold" in symptom or "cough" in symptom:
        return "General Physician"

    elif "chest" in symptom or "heart" in symptom:
        return "Cardiologist"

    elif "headache" in symptom or "brain" in symptom:
        return "Neurologist"

    elif "skin" in symptom or "allergy" in symptom:
        return "Dermatologist"

    elif "eye" in symptom:
        return "Ophthalmologist"

    elif "bone" in symptom or "joint" in symptom:
        return "Orthopedic"

    else:
        return "General Physician"
    
# Replace with your Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        age = int(request.form["age"])
        phone = request.form["phone"]
        symptom = request.form["symptom"]

        doctor = suggest_doctor(age, symptom)

        return render_template(
            "appointment.html",
            name=name,
            age=age,
            symptom=symptom,
            doctor=doctor
        )

    return render_template("register.html")

@app.route("/book", methods=["POST"])
def book():

    name = request.form["name"]
    doctor = request.form["doctor"]

    token = "HSP-" + str(len(appointments)+1).zfill(3)

    appointments.append({
        "token": token,
        "name": name,
        "doctor": doctor
    })

    return render_template(
        "success.html",
        token=token,
        name=name,
        doctor=doctor
    )

@app.route("/appointment", methods=["GET","POST"])
def appointment():

    if request.method == "POST":

        name = request.form["name"]
        department = request.form["department"]

        token = "HSP-" + str(len(appointments)+1).zfill(3)

        appointments.append({
            "token": token,
            "name": name,
            "department": department
        })

        return render_template(
            "success.html",
            token=token,
            name=name,
            department=department
        )

    return render_template("appointment.html")

@app.route("/queue")
def queue():

    current_serving = 1

    for i, patient in enumerate(appointments):

        patient["ahead"] = i

        patient["waiting_time"] = i * 5

    return render_template(
        "queue.html",
        appointments=appointments,
        current_serving=current_serving
    )
@app.route("/ask", methods=["POST"])
def ask():
    print("Request received")  # Test

    message = request.json["message"]

    response = model.generate_content(message)

    return jsonify({"reply": response.text})


@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    answer = ""

    if request.method == "POST":

        symptom = request.form["symptom"]

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            f"""
            Patient Symptoms:
            {symptom}

            Suggest hospital department and short advice.
            """
        )

        answer = response.text

    return render_template(
        "chatbot.html",
        answer=answer
    )

if __name__ == "__main__":
    app.run(debug=True)