class Doctor:
    def __init__(self, name, specialty, doctor_id):
        self.name = name
        self.specialty = specialty
        self.doctor_id = doctor_id
        self.appointment_schedule = []

    def add_appointment(self, appointment):
        self.appointment_schedule.append(appointment)

    def __str__(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}"
