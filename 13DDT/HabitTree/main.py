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
        self.root.geometry("850, 700")
        self.root.minimize("750, 600")
        self.root.configure(bg="#eef6ea")

        # User is loaded in once application starts
        self.data = load_data()

        # Stores usernname after a successful login
        self.current_user = None
        self.stage = 0

        self.userame_var = tk.StringVar()
        self.password_var = tk.StringVar()

        # Tree information
        