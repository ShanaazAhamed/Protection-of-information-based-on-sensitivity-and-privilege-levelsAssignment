import sys
from operations.display_details import Display
from roles.person import Person

class Pharmacist(Person):
    def __init__(self,user_id):
        super().__init__(user_id)

    def validate_id(self):
        return True

    def get_user_input(self):
        
        while True:
            try:
                user_input = int(input("1. View patient sickness details.\n2.View patient's drug_prescriptions details\n"))
                if user_input >0 and user_input<3:
                    break
                else:
                    print("Invalid Input")
            except KeyboardInterrupt:
                sys.exit(0)    
        return user_input


    def operation(self,db):
        patient_id = self.user[0]
        selection = self.get_user_input()
        if selection == 1:
            details = db.get_sickness_details(patient_id)
        elif selection == 2:
            details = db.get_drug_prescriptions(patient_id)
        
        if len(details) > 0:
            Display(details)
        else:
            print("No record found!")
        return