"""
EmpowerU

This file contains the class definition for the CourseMaterials class.
"""

# Third party imports
import tkinter as tk

class CourseMaterials(tk.Frame):
    def __init__(self, master, menu, user):
      
      super().__init__(master=master)
      self.master = master
      self.menu=menu
      self.user = user

      self.welcome_label = tk.Label(self, text=f"Welcome in, {user.first_name}!")
      self.welcome_label.pack(padx=10, pady=10)

      self.label1 = tk.Label(self, text="Choose one of the following:")
      self.label1.pack(padx=10, pady=10)

      self.register_btn = tk.Button(self, text="Artificial Intelligence", command=self.show_ai_materials)
      self.register_btn.pack(padx=10, pady=10)

      self.search_btn = tk.Button(self, text="Information Security", command=self.show_infosec_materials)
      self.search_btn.pack(padx=10, pady=10)

      self.class_btn = tk.Button(self, text="Python", command=self.show_python_materials)
      self.class_btn.pack(padx=10, pady=10)

      # Return to menu button
      self.return_button = tk.Button(self, text="Return to menu", command=self.return_to_menu)
      self.return_button.pack(padx=10, pady=10)
        
      
    def show_ai_materials(self):
       pass
    
    def show_infosec_materials(self):
       pass
    
    def show_python_materials(self):
       pass
    
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

