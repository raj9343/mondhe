from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define a structure to store appointment information
class Appointment:
    def __init__(self, patient_name, doctor_name, date, time):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.time = time

appointments = []

# Define the routes for the website
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/schedule", methods=["GET", "POST"])
def schedule():
    if request.method == "POST":
        # Get input for appointment information
        patient_name = request.form.get("patient_name")
        doctor_name = request.form.get("doctor_name")
        date = request.form.get("date")
        time = request.form.get("time")

        # Create a new appointment and add it to the list
        appointment = Appointment(patient_name, doctor_name, date, time)
        appointments.append(appointment)

        return redirect("/view")
    else:
        return render_template("schedule.html")

@app.route("/view")
def view():
    return render_template("view.html", appointments=appointments)

@app.route("/cancel", methods=["GET", "POST"])
def cancel():
    if request.method == "POST":
        # Get input for appointment to cancel
        patient_name = request.form.get("patient_name")

        # Find the appointment with the matching patient name
        cancel_index = -1
        for i, appointment in enumerate(appointments):
            if appointment.patient_name == patient_name:
                cancel_index = i
                break

        # If an appointment was found, remove it from the list
        if cancel_index != -1:
            appointments.pop(cancel_index)
            return redirect("/view")
        else:
            return render_template("cancel.html", message="No appointment found with that patient name.")
    else:
        return render_template("cancel.html", message="")

if __name__ == "__main__":
    app.run(debug=True)