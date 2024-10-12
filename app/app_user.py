class User:

    def __init__(self, uid, first_name, last_name, contact_num, contact_email="NO EMAIL"):
        """
        Constructor for the User class.
        """
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.contact_num = contact_num
        self.contact_email = contact_email

if __name__ == "__main__":
    pass
