# Habit Tree - Main Hub UI
# Displays the tree, daily controls, and statistics


import tkinter as tk
from tree import draw_tree

class HubUI:
    def __init__(self, app):
        self.app = app

    def show_hub(self):
        # Displays Habit Tree dashboard 
        self.app.clear_screen()

        user = self.app.data[self.app.current_user]
        stage = user["stage"]
        self.app.stage = stage

        today =  self.app.get_today()
        today_status = user["history"].get(today, "not_logged")

        # The header of window
        header = tk.Frame(self.app.root, bg="#315d2c", height=75)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="Habit Tree",
            bg="#315d2c",
            fg="white",
            font=("Arial", 22, "bold")
        ).pack(side="left", padx=25, pady=20)

        tk.Label(
            header,
            text=f"Welcome, {self.app.current_user}",
            bg="#315d2c",
            fg="#dbeed7",
            font=("Arial", 11)
        ).pack(side="left")

        self.app.make_button(
            header,
            "Logout",
            self.app.logout,
            10
        ).pack(side="right", padx=20, pady=16)

        # Main content
        content = tk.Frame(self.app.root, bg="#eef6ea")
        content.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=20
        )

        # The user's tree
        tree_frame = tk.Frame(
            content,
            bg="white",
            bd=1,
            relief="solid"
        )
        tree_frame.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 15)
        )

        tk.Label(
            tree_frame,
            text=f"stage {stage + 1} / {len(self.app.tree_stages)}",
            bg="white",
            fg="#6b9f5d",
            font=("Arial", 12, "bold")
        ).pack(pady=(15, 0))

        tk.Label(
            tree_frame,
            text=self.app.tree_stages[stage],
            bg="white",
            fg="#6b9f5d",
            font=("Arial", 24, "bold")
        ).pack()

        canvas = tk.Canvas(
            tree_frame,
            width=650,
            height=430,
            bg="#e8f3ff",
            highlightthickness=0
        )
        canvas.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

        draw_tree(canvas, stage)

        tk.Label(
            tree_frame,
            text=self.app.stage_descriptions[stage],
            bg="white",
            fg="#596653",
            font=("Arial", 11)
        ).pack(pady=(0, 15))

        # Daily controls
        side = tk.Frame(
            content,
            bg="#eef6ea",
            width=240
        )
        side.pack(side="right", fill="y")
        side.pack_propagate(False)

        card = tk.Frame(
            side,
            bg="white",
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )
        card.pack(fill="x", pady=(0, 15))

        tk.Label(
            card,
            text="TODAY",
            bg="white",
            fg="#315d2c",
            font=("Arial", 13, "bold")
        ).pack()

        if today_status == "not_logged":
            status_text = "Not logged today yet"
        elif today_status == "complete":
            status_text = "Completed today"
        else:
            status_text = "Missed"

        tk.Label(
            card,
            text=status_text,
            bg="white",
            fg="#526b50",
            font=("Arial", 12)
        ).pack(pady=(5))

        tk.Label(
            card,
            text="Did you complete your habit today?",
            bg="white",
            fg="#555555",
            wraplength=190,
            font=("Arial", 10)
        ).pack(pady=(5, 12))

        complete_button = self.app.make_button(
            card,
            "Yes - I DID IT",
            lambda: self.app.habit_manager.log_habit(True),
            20
        )
        complete_button.pack(pady=4)

        missed_button = tk.Button(
            card,
            text="NO - NOT TODAY",
            command=lambda: self.app.habit_manager.log_habit(False),
            width=20,
            font=("Arial", 10, "bold"),
            bg="#d8ddd6",
            fg="#455145",
            padx=8,
            pady=7,
            cursor="hand2"
        )
        missed_button.pack(pady=4)

        if today_status != "not_logged":
            complete_button.config(state="disabled")
            missed_button.config(state="disabled")

        # Stats card
        stats = tk.Frame(
            side,
            bg="white",
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )
        stats.pack(fill="x")

        streak = self.app.habit_manager.calculate_streak()

        tk.Label(
            stats,
            text="YOUR STATS",
            bg="white",
            fg="#315d2c",
            font=("Arial", 12, "bold")
        ).pack(pady=(0, 8))

        # Stage stats
        tk.Label(
            stats,
            text=f"Current stage: {stage + 1} / {len(self.app.tree_stages)}",
            bg="white",
            anchor="w",
            font=("Arial", 10)
        ).pack(fill="x")

        # Streak Stats
        tk.Label(
            stats,
            text=f"Current streak: {streak} day(s)",
            bg="white",
            anchor="w",
            font=("Arial", 10)
        ).pack(fill="x")

        # Longest streak
        tk.Label(
            stats,
            text=f"Longest streak: {user['longest_streak']}",
            bg="white",
            anchor="w",
            font=("Arial", 10)
        ).pack(fill="x")

        # Total completed
        tk.Label(
            stats,
            text=f"Total completed: {user['total_completed']}",
            bg="white",
            anchor="w",
            font=("Arial", 10)
        ).pack(fill="x")

        self.app.make_button(
            stats,
            "View Progress History",
            self.app.show_history,
            20
        ).pack(pady=(15, 2))

        # Footer
        tk.Label(
            self.app.root,
            text="Small actions have big impacts...",
            bg="#eef6ea",
            fg="#71806e",
            font=("Arial", 9, "italic")
        ).pack(pady=(0, 8))  