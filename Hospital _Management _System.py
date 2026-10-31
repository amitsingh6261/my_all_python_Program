
patients = []
doctors = {
    1: {"name": "Dr. Sharma", "speciality": "Heart Specialist"},
    2: {"name": "Dr. Verma", "speciality": "Dentist"},
    3: {"name": "Dr. Singh", "speciality": "General Physician"}
}

appointments = []

while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Register Patient")
    print("2. View Doctors")
    print("3. Book Appointment")
    print("4. View Patients")
    print("5. Generate Hospital Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        disease = input("Enter disease: ")

        patient = {
            "name": name,
            "age": age,
            "disease": disease
        }

        patients.append(patient)
        print("Patient registered successfully!")

    elif choice == "2":
        print("\n----- DOCTOR DETAILS -----")

        for doctor_id, doctor in doctors.items():
            print(doctor_id, doctor["name"])
            print("Speciality:", doctor["speciality"])

    elif choice == "3":
        if len(patients) == 0:
            print("Please register a patient first.")

        else:
            print("\nRegistered Patients:")

            for i, patient in enumerate(patients):
                print(i + 1, patient["name"])

            patient_id = int(input("Select patient number: "))
            doctor_id = int(input("Enter doctor ID: "))

            if 1 <= patient_id <= len(patients) and doctor_id in doctors:
                appointment = {
                    "patient": patients[patient_id - 1]["name"],
                    "doctor": doctors[doctor_id]["name"]
                }

                appointments.append(appointment)
                print("Appointment booked successfully!")

            else:
                print("Invalid patient or doctor ID!")

    elif choice == "4":
        print("\n----- PATIENT RECORDS -----")

        if not patients:
            print("No patient records found.")

        else:
            for patient in patients:
                print("Name:", patient["name"])
                print("Age:", patient["age"])
                print("Disease:", patient["disease"])
                print("----------------------")

    elif choice == "5":
        if not patients:
            print("No patient records found.")

        else:
            print("\n----- PATIENT LIST -----")

            for i, patient in enumerate(patients):
                print(i + 1, patient["name"])

            patient_id = int(input("Select patient number: "))

            if 1 <= patient_id <= len(patients):
                consultation = 500
                medicine = float(input("Enter medicine charges: "))
                room = float(input("Enter room charges: "))

                total = consultation + medicine + room

                print("\n========== HOSPITAL BILL ==========")
                print("Patient:", patients[patient_id - 1]["name"])
                print("Consultation: Rs.", consultation)
                print("Medicine: Rs.", medicine)
                print("Room Charges: Rs.", room)
                print("----------------------------------")
                print("Total Bill: Rs.", total)

            else:
                print("Invalid patient number!")

    elif choice == "6":
        print("Thank you for using Hospital Management System!")
        break

    else:
        print("Invalid choice! Try again.")
