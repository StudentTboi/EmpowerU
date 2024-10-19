import tkinter as tk
import app.app_utils as util
from functools import partial
from app.app_course import Course
from interface.gui_learning_content import ReadingMaterialMenu
from interface.gui_do_quiz_menu import DoQuiz

class CourseMenu(tk.Frame):
    def __init__(self, master, menu, user, course):
        super().__init__(master=master)
        self.master = master
        self.menu=menu
        self.user = user
        self.course = course

        self.label1 = tk.Label(self, text="Choose one of the following:")
        self.label1.pack(padx=10, pady=10)


        self.search_btn = tk.Button(self, text="Learning Content", command=self.show_learning_content_page)
        self.search_btn.pack(padx=10, pady=10)

        self.class_btn = tk.Button(self, text="Quiz", command=self.show_quiz_content_page)
        self.class_btn.pack(padx=10, pady=10)
        
        # Return to menu button
        self.return_button = tk.Button(self, text="Return to course menu", command=self.return_to_menu)
        self.return_button.pack(padx=10, pady=10)

    def show_learning_content_page(self):
        reading_materials = ReadingMaterialMenu(self.master, self, self.user, self.course)
        reading_materials.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()

    def hide_menu(self):
        """
        Method to hide the menu frame.
        """
        self.place_forget()

    def show_quiz_content_page(self):
        quiz_content = DoQuiz(self.master, self, self.user, self.course)
        quiz_content.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.hide_menu()
    
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
