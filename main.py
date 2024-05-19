from patient import Patient
from doctor import Doctor
from appointment import Appointment
def main():

    #create a patient
    patient1 = Patient("Gayani", 60, "P001")
    patient1.add_medical_record("2024-05-11: Consultation")
    patient1.add_medical_record("2024-04-20: Checkup")

    # create a doctor
    doctor1 = Doctor("Dr. Julian", "Dermatology", "D001")
    doctor1.add_appointment("2024-06-01, 10:00 AM")

    #create a appointment
    appointment1 = Appointment(patient1,doctor1,"2024-05-28","11:00 PM")

    # print patient and doctor details
    print(patient1)
    print(doctor1)
    print(appointment1)

if __name__ == "__main__":
    main()
