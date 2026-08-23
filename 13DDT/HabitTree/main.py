# Habit Tree - Main Program
# Year 13 Digital Technology Project

import tkinter as tk
from tkinter import messagebox
from datetime import date

from data_manager import load_data
from habit_manager import HabitManager
from tree import TREE_STAGES, STAGE_DESCRIPTIONS
from ui.login import LoginUI
from ui.history import HistoryUI
from ui.hub import HubUI

class HabitTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Habit Tree")
        self.root.geometry("850x700")
        self.root.minsize(750, 600)
        self.root.configure(bg="#eef6ea")

        # User is loaded in once application starts
        self.data = load_data()

        # Stores username after a successful login
        self.current_user = None
        self.stage = 0

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Tree information
        self.tree_stages = TREE_STAGES
        self.stage_descriptions = STAGE_DESCRIPTIONS

        # Managers deal with the data and UI
        self.habit_manager = HabitManager(self)
        self.login_ui = LoginUI(self)
        self.history_ui = HistoryUI(self)
        self.hub_ui = HubUI(self)

        self.show_login()


    # Gui helpers
    def clear_screen(self):
        # Removes the current window
        for widget in self.root.winfo_children():
            widget.destroy()

    def make_button(self, parent, text, command, width=18):
        # Creates a consistent button for the app
        return tk.Button(
           parent,
           text=text,
           command=command,
           width=width,
           font=("Arial", 11, "bold"),
           bg="#6b9f5d",
           fg="white",
           activebackground="#57864c",
           activeforeground="white",
           relief="flat",
           padx=8,
           pady=8,
           cursor="hand2"
        )

    def show_error(self, title, message):
        messagebox.showerror(title, message)

    def show_info(self, title, message):
        messagebox.showinfo(title, message)

    def get_today(self):
        return str(date.today())

    # Navigation
    def show_login(self):
        self.login_ui.show_login()

    def show_hub(self):
            self.hub_ui.show_hub()

    def show_history(self):
            self.history_ui.show_hitory()

    def logout(self):
        self.current_user = None
        self.stage = 0
        self.username_var.set("")
        self.password_var.set("")
        self.show_login()

# Starting the program up
if __name__ == "__main__":
     root = tk.Tk()
     app = HabitTreeApp(root)
     root.mainloop()