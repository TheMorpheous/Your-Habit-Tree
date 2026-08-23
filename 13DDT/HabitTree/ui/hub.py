# Habit Tree - Main Hub UI
# Displays the tree, daily controls, and statistics


import tkinter as tk
from tree import draw_tree

class HubUI:
    def __init__(self, app):
        self.app = app

    def show_hub(self):
        