class Appointment:
    def _init_(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def _str_(self):
        return (f"Appointment Details:\n"
                f"Patient: {self.patient.name}, Doctor: {self.doctor.name}\n"
                f"Date: {self.date}, Time: {self.time}")
