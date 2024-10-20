class User:
    def __init__(self, uid, first_name, last_name, date_of_birth, contact_num, contact_email, username, password):
        """
        Constructor for the User class.
        
        Parameters:
        - uid (str): Unique identifier for the user.
        - first_name (str): The user's first name.
        - last_name (str): The user's last name.
        - date_of_birth (str): The user's date of birth.
        - contact_num (str): The user's contact number.
        - contact_email (str): The user's email address.
        - username (str): The user's username for authentication.
        - password (str): The user's password for authentication.
        """
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.contact_num = contact_num
        self.contact_email = contact_email
        self.username = username
        self.password = password

if __name__ == "__main__":
    pass
