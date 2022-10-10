
import json
import uuid
from datetime import datetime

class DataBase:
    def __init__(self):
        self.load_db()


    def load_db(self):
        with open('records.json', 'r') as records:
        # Reading from json file
            json_object = json.load(records)
            self.db = json_object


    def get_personal_details(self,patient_id):
        data = []
        data_records = {'personal':1, 'sickness':2, 'drug_prescriptions':3, 'test_prescriptions':4}
        for key in self.db:
            try:
                if self.db[key]["patient_id"] == patient_id and str(self.db[key]['record_type']) == str(data_records["personal"]):
                    data.append(self.db[key])
            except:
                print("Database Error")
                continue
        return data

    def get_sickness_details(self,patient_id):
        data = []
        data_records = {'personal':1, 'sickness':2, 'drug_prescriptions':3, 'test_prescriptions':4}
        for key in self.db:
            try:
                if self.db[key]["patient_id"] == patient_id and str(self.db[key]['record_type']) == str(data_records['sickness']):
                    data.append(self.db[key])
            except:
                print("Database Error")
                continue
        return data

    def get_drug_prescriptions(self,patient_id):
        data = []
        data_records = {'personal':1, 'sickness':2, 'drug_prescriptions':3, 'test_prescriptions':4}
        for key in self.db:
            try:
                if self.db[key]["patient_id"] == patient_id and str(self.db[key]['record_type'])==str(data_records['drug_prescriptions']):
                    data.append(self.db[key])
            except:
                print("Database Error")
                continue
        return data            

    def get_lab_test_prescriptions(self,patient_id):
        data = []
        data_records = {'personal':1, 'sickness':2, 'drug_prescriptions':3, 'test_prescriptions':4}
        for key in self.db:
            try:
                if self.db[key]["patient_id"] == patient_id and str(self.db[key]['record_type'])==str(data_records['test_prescriptions']):
                    data.append(self.db[key])
            except:
                print("Database Error")
                continue
        return data 


    def write_record(self,patient_id,patient_name,record_type,sens_level,data):
        data_records = {1:'personal', 2:'sickness',3: 'drug_prescriptions', 4:'test_prescriptions'}
        key = str(uuid.uuid4())
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        record = data_records[record_type]
        try:
            self.db[key] = {"patient_id":patient_id,"patient_name":patient_name,"record_type":record,"sens_level":sens_level,"data":data,"Date":date_time}
            print("Data Added Successfully")
            with open('records.json', 'w') as f:
                json.dump(self.db, f)
                f.close()
        except:
            print("Error Occurs")
