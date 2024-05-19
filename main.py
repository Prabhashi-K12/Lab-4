from patient import Patient
from doctor import Doctor
def main():
    patient1 = Patient("Gayani", 60, "P001")
    doctor1 = Doctor("Dr. Julian", "Dermatology", "D001")

    print(patient1)
    print(doctor1)

if __name__ == "__main__":
    main()
