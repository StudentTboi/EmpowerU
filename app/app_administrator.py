import os

from app.app_user import User
from app.app_lecturer import LecturerUser

class AdministratorUser(User):
    @staticmethod
    def authenticate(input_username, input_password):
        admin_path = "./authenticate/admins.txt"
        if os.path.exists(admin_path):
            with open(admin_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                if len(line)<5: #Checking if line is invalid
                    print(f"WARNING: A line in {admin_path} is invalid")
                    continue
                
                admin_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return AdministratorUser(admin_id, first_name, last_name, contact_num, input_username, input_password)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {admin_path} exists.")

    def __init__(self, uid, first_name, last_name, contact_num, username, password):
        super().__init__(uid, first_name, last_name, contact_num)
        self.username = username
        self.password = password
