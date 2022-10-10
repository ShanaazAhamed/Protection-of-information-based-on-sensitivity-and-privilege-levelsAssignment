import sys
from operations.display_details import Display
from operations.add_new_patient import add_new_patient
from roles.person import Person

class Lab_Assistant(Person):
    def __init__(self,user_id):
        super().__init__(user_id)

    def validate_id(self):
        return True

    def get_user_input(self):
        while True:
            try:
                user_input = int(input("\n1.View test prescriptions.\n2.Add lab test prescriptions\n"))
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
            details = db.get_lab_test_prescriptions(patient_id)

        elif selection == 2:
            lab_test_prescriptions = input("Enter ab_test_prescriptions details: ")
            db.write_record(patient_id,self.user[1],4,4,lab_test_prescriptions)
            return
            
        if len(details) > 0:
            Display(details)
        else:
            print("No record found!")
        return