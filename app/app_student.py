"""
FIT1056 EMPOWERU
"""
from app_lecturer import User

class StudentUser(User):
  def __init__(self, uid, first_name, last_name, date_of_birth, contact_name, contact_num):
    """
    Constructor
    """
    super().__init__(uid, first_name, last_name, contact_num)
    self.date_of_birth = date_of_birth
    self.contact_name = contact_name

if __name__ == "__main__":
  pass
