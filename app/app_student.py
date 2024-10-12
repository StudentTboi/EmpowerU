"""
FIT1056 EMPOWERU
"""
import os

from app.app_lecturer import User

class StudentUser(User):
    @staticmethod
    def authenticate(input_username, input_password):
        student_path = "./authenticate/students.txt"
        if os.path.exists(student_path):
            with open(student_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                if len(line)<5: #Checking if line is invalid
                    print(f"WARNING: A line in {student_path} is invalid")
                    continue
                
                student_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return StudentUser(student_id, first_name, last_name, contact_num, input_username, input_password)
                    else:
                        return None # or return, or break
                else:
                    print(f"Please check subdirectory and file {student_path} exists.")

    def __init__(self, uid, first_name, last_name, date_of_birth, contact_name, contact_num):
        """
        Constructor
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.date_of_birth = date_of_birth
        self.contact_name = contact_name

if __name__ == "__main__":
  pass
