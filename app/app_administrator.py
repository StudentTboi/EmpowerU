import os

from app.app_user import User
from app.app_lecturer import LecturerUser


class AdministratorUser(User):
  @staticmethod
  def authenticate(input_user, input_password):
    recept_path = "./authenticate/admin.txt"
    if os.path.exists(recept_path):
      with open(recept_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                 recept_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return ReceptionistUser(recept_id, first_name, last_name, contact_num, input_username, input_password)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {recept_path} exists.")

def __init__(self, uid, first_name, last_name, contact_num, username, password):
          super().__init__(uid, first_name, last_name, contact_num)
        self.username = username
        self.password = password
        
    
