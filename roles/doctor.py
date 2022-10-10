import sys
from operations.display_details import Display
from roles.person import Person

class Doctor(Person):
    def __init__(self,user_id):
        super().__init__(user_id)

    def validate_id(self):
        return True

    def get_user_input(self):
        
        while True:
            try:
                user_input = int(input("1. View patient personal details.\n2. View patient sickness details.\n3.View patient's drug_prescriptions details\n4.View patient's lab_test_prescriptions\n5.Edit patient sickness details\n6.Edit patient's drug_prescriptions details\n"))
                if user_input >0 and user_input<7:
                    break
                else:
                    print("Invalid Input!")
            except KeyboardInterrupt:
                sys.exit(0)    
        return user_input


    def operation(self,db):
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
        elif selection == 5:
            sickness = input("Enter sickness details: ")
            db.write_record(patient_id,self.user[1],2,1,sickness)
            return
        elif selection == 6:
            drug_prescriptions = input("Enter drug prescriptions details: ")
            db.write_record(patient_id,self.user[1],2,3,drug_prescriptions)
            return
        if len(details) > 0:
            Display(details)
        else:
            print("No record found!")
        return