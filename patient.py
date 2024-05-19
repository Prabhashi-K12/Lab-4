class Patient:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.medical_history = []

    def add_medical_record(self, record):
        self.medical_history.append(record)

    def __str__(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}"
