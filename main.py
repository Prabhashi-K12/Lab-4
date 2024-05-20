from patient import Patient
from doctor import Doctor
from appointment import Appointment
def main():

    #create a patient
    patient1 = Patient("Gayani", 60, "P001")
    patient1.add_medical_record("2024-05-11: Consultation")
    patient1.add_medical_record("2024-04-20: Checkup")
    patient2 = Patient("Chandika Sandun", 23,"P002")
    patient2.add_medical_record("2024-05-19: Surgery")
    patient2.add_medical_record("2024-03-07: Scan")

    # create a doctor
    doctor1 = Doctor("Dr. Julian", "Dermatology", "D001")
    doctor1.add_appointment("2024-06-01, 10:00 AM")
    doctor2 = Doctor("Dr. Madusha","Surgeon","D002")
    doctor2.add_appointment("2024-05-23, 02:00 PM")
    

    #create an appointment
    appointment1 = Appointment(patient1,doctor1,"2024-05-28","11:00 PM")
    appointment2 = Appointment(patient2,doctor2,"2024-06-10", "10:00 AM")

    # print patient and doctor details
    print(patient1)
    print(doctor1)
    print(appointment1)
    print(patient2)
    print(doctor2)
    print(appointment2)

if __name__ == "__main__":
    main()
