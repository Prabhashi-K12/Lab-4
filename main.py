from patient import Patient
def main():
    #create a patient
    patient1 = Patient("Gayani", 60, "P001")
    patient1.add_medical_record("2024-05-11: Consultation")
    patient1.add_medical_record("2024-04-20: Checkup")

    print(patient1)

if __name__ == "__main__":
    main()
