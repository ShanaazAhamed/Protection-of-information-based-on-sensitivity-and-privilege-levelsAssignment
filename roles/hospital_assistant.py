import sys
from operations.display_details import Display
from operations.add_new_patient import add_new_patient
from roles.person import Person

class Hospital_Assistant(Person):
    def __init__(self,user_id):
        super().__init__(user_id)

    def validate_id(self):
        return True

    def get_user_input(self):
        while True:
            try:
                user_input = int(input("1. View patient personal details.\n2.View patient sickness details.\n3.Add a new patient\n"))
                if user_input >0 and user_input<4:
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
            details = db.get_personal_details(patient_id)
        elif selection == 2:
            details = db.get_sickness_details(patient_id)
        elif selection == 3:
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            role = input("Enter the role: ")
            new_patient =  add_new_patient(username,password,role)
            if new_patient.write():
                print('Successfully added')
                return
            else:
                print('username already exist')
                return
            
        if len(details) > 0:
            Display(details)
        else:
            print("No record found!")
        return