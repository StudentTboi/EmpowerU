import tkinter as tk
import app.app_utils as util

class Editor(tk.Frame):
    
    def __init__(self, master, menu, user, course, part_to_edit):
        super().__init__(master=master)
        self.master = master
        self.menu=menu
        self.user = user
        self.filename = f"{course.filepath}/{part_to_edit}.txt"
        self.data = util.read_file(self.filename)

        # Return to menu button
        self.return_button = tk.Button(self, text="Return to course menu", command=self.return_to_menu)
        # Create text widget and specify size.
        self.text_to_edit = tk.Text(self, height = 20, width = 60)
        # Create button for next text.
        self.save_button = tk.Button(self, text = "Save", command=self.save_file)

        self.text_to_edit.pack()
        self.save_button.pack()
        self.return_button.pack()

        # Insert The Fact.
        for line in self.data:
            self.text_to_edit.insert(tk.END, line)
        self.data=self.text_to_edit
        

    def save_file(self):
        INPUT = self.text_to_edit.get("1.0", "end-1c")
        with open(self.filename,"w") as filetowrite:
            for lines in INPUT:
                filetowrite.write(lines)

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