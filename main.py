import sys
from database import DataBase
from roles.doctor import Doctor
from roles.hospital_assistant import Hospital_Assistant
from roles.lab_assistant import Lab_Assistant
from roles.patient import Patient
import csv
import hashlib

from roles.pharmacist import Pharmacist

class User:
    def __init__(self):
         self.logged = False
         self.username= ""
         self.password = ""
         self.user_id = ""
         self.user_type = 0

    def read_from_user_data(self):
        with open('user_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for user in reader:
                if user[1] == self.username:
                    hashed_password = user[2]
                    if(hashlib.md5(self.password.encode('utf-8')).hexdigest() == hashed_password):
                        return user[0], int(user[3])
                    return -1,0
                continue
        return -1,-1
   
    def roles(self):
        if self.user_type > 1:
            patient_id = input("Enter Patient ID: \n")
            self.patient_id = patient_id
        db = DataBase()
        try:
            if user.user_type == 1:
                patient = Patient(self.user_id)
                patient.personal_details(db)
            elif user.user_type == 2:
                hos_assistant = Hospital_Assistant(self.patient_id)
                hos_assistant.operation(db)
            elif user.user_type == 3:
                pharmacist = Pharmacist(self.patient_id)
                pharmacist.operation(db) 
            elif user.user_type == 4:
                lab_assistant = Lab_Assistant(self.patient_id)
                lab_assistant.operation(db)   
            elif user.user_type == 5:
                doctor = Doctor(self.patient_id)
                doctor.operation(db)   
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    user = User()
    while True:
        if user.logged == False:
            user_name = input("Enter the username: ").strip()
            password = input("Enter your password: ").strip()
            user.username = user_name
            user.password  = password
            user_id,user_type = user.read_from_user_data()
            if user_type == 0:
                print("Invalid Password!")
                user.logged = False
                continue
            elif user_id == 0:
                user.logged = False
                print("Invalid username")
                continue
            elif user_type < 0:
                user.logged = False
                print("No Such file found!")
                continue
            user.logged = True
            user.user_id = user_id
            user.user_type = user_type
            print(f"Welcome {user.username}")

        else:
            if user.user_type > 0:
                user.roles()
            else:
                print("Invalid login!, Please login again!")
                continue

    


    