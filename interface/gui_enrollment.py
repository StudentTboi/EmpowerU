import tkinter as tk

class Enroll(tk.Frame):
    def __init__(self, master, menu, user, student):
        super().__init__(master=master)
        self.master = master
        self.menu=menu
        self.user = user
        self.student=student

        self.user_detail_label = tk.Label(self, text=f" {self.student.first_name} {self.student.last_name}'s Enrollment")
        self.user_detail_label.grid(row=0, columnspan=2, padx=10, pady=10, sticky=tk.E)

        # Specialization label widget
        self.password_label = tk.Label(master=self, text="Specialization:")
        self.password_label.grid(row=2, columnspan=2, padx=10, pady=10, sticky=tk.S)
        self.ai_check_var = tk.IntVar()
        self.ai_check_bt = tk.Checkbutton(master=self, text='Artificial Intelligence', variable=self.ai_check_var, onvalue=1, offvalue=0)
        self.ai_check_bt.grid(row=3, columnspan=2, padx=10, pady=10, sticky=tk.W)
        
        self.infosec_check_var = tk.IntVar()
        self.infosec_check_bt = tk.Checkbutton(master=self, text='Information Security', variable=self.infosec_check_var, onvalue=1, offvalue=0)
        self.infosec_check_bt.grid(row=4, columnspan=2, padx=10, pady=10, sticky=tk.W)
        
        self.pylearn_check_var = tk.IntVar()
        self.pylearn_check_bt = tk.Checkbutton(master=self, text='Python Learning', variable=self.pylearn_check_var, onvalue=1, offvalue=0)
        self.pylearn_check_bt.grid(row=5, columnspan=2, padx=10, pady=10, sticky=tk.W)

        self.enroll_button = tk.Button(master=self, text="Enroll", command=self.enroll_unit)
        self.enroll_button.grid(row=7, columnspan=2, padx=10, pady=10, sticky=tk.S)

        # Alert variable and label widget
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var)
        self.alert_label.grid(row=9, columnspan=2, sticky=tk.S, padx=10, pady=10)
        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=30, columnspan=2, padx=10, pady=10, sticky=tk.N)
        
    def enroll_unit(self):
        specialization_list = []
        if self.ai_check_var.get() == 1:
            specialization_list.append("AI")
        if self.infosec_check_var.get() == 1:
            specialization_list.append("InfoSec")
        if self.pylearn_check_var.get() == 1:
            specialization_list.append("PyLearn")

        if self.user.edit_student_data(self.student, specialization=specialization_list):
            self.alert_var.set("Successfully enrolled student's unit")
            self.ai_check_bt.deselect()
            self.infosec_check_bt.deselect()
            self.pylearn_check_bt.deselect()

        else:
            self.alert_var.set("ERROR")

        

    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.menu.place(relx=.5, rely=.5, anchor=tk.CENTER)


