import os
from app.app_user import User

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
        recept_path = "./data/pst4_receptionists.txt"
        if os.path.exists(recept_path):
            with open(recept_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                lecturer_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return ReceptionistUser(recept_id, first_name, last_name, contact_num, input_username, input_password)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {recept_path} exists.")
          
    def __init__(self, uid, first_name, last_name, contact_num, teaching_area):
        """
        Constructor for the TeacherUser class
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.teaching_area = teaching_area


if __name__ == "__main__":
    pass
