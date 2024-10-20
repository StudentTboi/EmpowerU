import tkinter as tk

class DoQuiz(tk.Frame):
    def __init__(self, master, student_menu, student_user, course):
        """
        Constructor for the SearchTeachers class.

        Parameters:
        - master: master widget of this widget instance
        - receptionist_menu: an instance of the ReceptionistMenu class
        - receptionist_user: an instance of the ReceptionistUser class
        """
        super().__init__(master)
        self.master = master
        self.student_menu = student_menu
        self.student_user = student_user
        self.quiz = course.quiz

        self.answer_entry = []
        self.answer_var = []
        self.question_label = []
        for index,question in enumerate(self.quiz.questions):
            self.question_label.append(tk.Label(master=self, text=question, justify="left"))
            self.answer_var.append(tk.StringVar(master=self))
            self.answer_entry.append(tk.Entry(master=self, textvariable=self.answer_var[index]))
            self.question_label[index].grid(row=index*2+1, column=0, sticky=tk.W)
            self.answer_entry[index].grid(row=index*2+2, column=0, sticky=tk.W)
        self.pack()

        self.submit_button = tk.Button(master=self, text="Submit", command=self.submit_quiz)
        self.submit_button.grid(row=2 * len(self.quiz.questions), column=0, padx=10, pady=10, sticky=tk.E)

        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
        self.return_button.grid(row=2 * len(self.quiz.questions) + 1, columnspan=2, padx=10, pady=10, sticky=tk.E)

    def submit_quiz(self):
        answers = []
        for answer_var in self.answer_var:
            answers.append(answer_var.get())
        self.quiz.gradeQuiz(answers, self.student_user.uid)
    
    def return_to_menu(self):
        """
        This method handles the GUI logic to return to the receptionist's menu.

        Parameters:
        (None)

        Returns:
        (None)
        """
        self.place_forget()
        self.student_menu.place(relx=.5, rely=.5, anchor=tk.CENTER)
            
            
        
        
        