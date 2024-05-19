from patient import Patient
from doctor import Doctor
def main():
    # create a patient
    patient1 = Patient("Gayani", 60, "P001")

    # create a doctor
    doctor1 = Doctor("Dr. Julian", "Dermatology", "D001")
    doctor1.add_appointment("2024-06-01, 10:00 AM")

    print(patient1)
    print(doctor1)

if __name__ == "__main__":
    main()
