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

