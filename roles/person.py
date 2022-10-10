import csv
class Person:
    def __init__(self,user_id):
        self.load_detail(user_id)

    def load_detail(self,user_id):
        with open('user_data.csv', 'r') as file:
            reader = csv.reader(file)
            for user in reader:
                if user[0] == user_id:
                    self.user = user
                    return
            return None
