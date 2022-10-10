from csv import reader,writer
import hashlib
import uuid

class add_new_patient:
    def __init__(self,username,password,role):
       self.username = username
       self.password = password
       self.role = role

    def write(self):
        hashed_password = hashlib.md5(self.password.encode('utf-8')).hexdigest() 

        with open('user_data.csv', 'r') as file:
            rows = reader(file)
            for user in rows:
                if user[1] == self.username:
                    return False
            file.close()

        data_row=[str(uuid.uuid4()),self.username,hashed_password,self.role]
        field_names = ['id','username','password','role']
        data_dict = {'id':str(uuid.uuid4()),'username':self.username,'password':hashed_password,'role':self.role}

        with open('user_data.csv', 'a',newline='') as csv_file:
            csv_writer = writer(csv_file)
            csv_writer.writerow(data_row)
            csv_file.close()
            return True