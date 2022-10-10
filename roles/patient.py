
import sys
from operations.display_details import Display
from roles.person import Person

class Patient(Person):
    def __init__(self,user_id):
        super().__init__(user_id)

    def validate_id(self):
        return True

    def get_user_input(self):
        
        while True:
            try:
                user_input = int(input("\nPlease  enter only the relevant integer preceding the options to make choice.\nYou can view your records.\n1. View Personal Details.\n2. View All Sickness Details.\n3. View All Drug Prescription Details.\n4. View All Lab Test Prescription Details.\n"))
                if user_input > 0 and user_input <5:
                    break
                else:
                    print("Invalid Input!")
            except KeyboardInterrupt:
                sys.exit(0)

        return user_input


    def personal_details(self,db):
        details = []
        patient_id = self.user[0]
        selection = self.get_user_input()
        if selection == 1:
            details = db.get_personal_details(patient_id)
        elif selection == 2:
            details = db.get_sickness_details(patient_id)
        elif selection == 3:
            details = db.get_drug_prescriptions(patient_id)
        elif selection == 4:
            details = db.get_lab_test_prescriptions(patient_id)  
        else:
            print("Invalid Input")

        if len(details) > 0:
            Display(details)
        else:
            print("No record found!")