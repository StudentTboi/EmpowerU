"""
EmpowerU

This file contains the function definition to run the GUI application.
"""

# Third party imports
import tkinter as tk

# Local application imports
from interfaces.gui_main_window import EMPU

def main():
    """
    The main function definition.

    Parameters:
    (None)

    Returns:
    (None)
    """
    root = EMPU(title="EmpowerU Learning Platform", width=720, height=480)
    root.mainloop()
    print("EMPU proper shutdown completed.")


if __name__ == "__main__":
    # DO NOT MODIFY
    main()
