import os
from app.app_user import User
from app.app_student import StudentUser

class LecturerUser(User):

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Method to authenticate a lecturer user.

        Parameter(s):
        - input_username: str
        - input_password: str

        Returns:
        - an instance of LecturerUser corresponding to the username if successful,
          None otherwise
        """
        lecturer_path = "./authenticate/lecturers.txt"
        if os.path.exists(lecturer_path):
            with open(lecturer_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()

            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                if len(line)<5: #Checking if line is invalid
                    print(f"WARNING: A line in {lecturer_path} is invalid")
                    continue
                
                lecturer_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return LecturerUser(lecturer_id, first_name, last_name, contact_num, input_username, input_password)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {lecturer_path} exists.")
          
    def __init__(self, uid, first_name, last_name, contact_num, teaching_area):
        """
        Constructor for the LecturerUser class
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.teaching_area = teaching_area

    def import_students_data(self):
        """
        Method to read students data and store it into the lecturer's session.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.students = []
        students_path = "./data/pst4_students.txt"
        if os.path.exists(students_path):
            with open(students_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
                for line in lines:
                    student_id, first_name, last_name, date_of_birth, contact_name, contact_num = line.strip("\n").split(",")
                    student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_name, contact_num)
                    self.students.append(student_obj)
        else:
            print(f"Please check the subdirectory and file exists for {students_path}.")

if __name__ == "__main__":
    pass
