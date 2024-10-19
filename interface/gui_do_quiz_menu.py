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
            self.question_label.append(tk.Label(master=self, text=question))
            self.answer_var.append(tk.StringVar(master=self))
            self.answer_entry.append(tk.Entry(master=self, textvariable=self.answer_var[index]))
            self.question_label[index].grid(row=index*2+1, column=0, sticky=tk.W)
            self.answer_entry[index].grid(row=index*2+2, column=0, sticky=tk.W)
        self.pack()
            
            
        
        
        