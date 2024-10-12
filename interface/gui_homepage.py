"""
EmpowerU
This file contains the class definition for the HomePage class.
"""

# Third party imports
import tkinter as tk

# Local application imports
from app.app_administrator import AdministratorUser
from interfaces.gui_administrator_menu import AdministratorMenu

class HomePage(tk.Frame):

    def __init__(self, master, image_path):
        """
        Constructor for the HomePage class.

        Parameter(s):
        - master: master widget of this widget instance
        - image_path: str, path of the logo image file
        """
        super().__init__(master=master)
        self.master = master 
        self.image_path = image_path

        # Image obtained from: 
        # https://pngtree.com/freepng/red-blue-separation-line-musical-music-logo_6244544.html

        # Logo image
        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self, image=self.logo_photoimage, width=128, height=128)
        self.logo_label.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        # Welcome heading
        self.login_title = tk.Label(master=self, \
            text="Welcome to EmpowerU Learning Platform", \
            font=("Arial Bold", 20))
        self.login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        # Username label widget
        self.username_label = tk.Label(master=self, text="Username:")
        self.username_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        # Username variable and entry widget
        self.username_var = tk.StringVar(master=self)
        self.username_entry = tk.Entry(master=self, textvariable=self.username_var)
        self.username_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Password label widget
        self.password_label = tk.Label(master=self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        # Password variable and entry widget
        self.password_var = tk.StringVar(master=self)
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="●")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Alert variable and label widget - displays alert messages where necessary
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var)
        self.alert_label.grid(row=4, columnspan=2, padx=10, pady=10)

        # Button to login
        self.login_button = tk.Button(master=self, text="Login", command=self.login)
        self.login_button.grid(row=5, columnspan=2, padx=10, pady=10)

        # Button to shut down
        self.shutdown_button = tk.Button(master=self, text="Shut down", command=master.destroy)
        self.shutdown_button.grid(row=6, columnspan=2, padx=10, pady=10)

    def login(self):
        """
        Method to handle the login upon button click.

        Parameter(s):
        (None)

        Return(s):
        (None)
        """

        administrator_user = AdministratorUser.authenticate(self.username_var.get(), self.password_var.get())
        # Checks if receptionist_user is an instance of the AdministratorUser class (i.e. authentication is successful)
        # https://docs.python.org/3/library/functions.html#isinstance
        if isinstance(administrator_user, AdministratorUser):
            # TODO: Complete this block; Hint: self.master is a very useful instance variable
            self.alert_var.set("")
            menu= AdministratorMenu(self.master, administrator_user)
            menu.show_menu()
            self.master.hide_homepage()
        else:
            # TODO: Complete this block
            self.alert_var.set("Wrong Username or password!")
        self.username_entry.delete(0,"end")
        self.password_entry.delete(0,"end")
        
if __name__ == "__main__":
    pass
