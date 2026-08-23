# Habit Tree - History UI
# Displays the user's previous daily habit results


import tkinter as tk

class HistoryUI:
    def __init__(self, app):
        self.app = app

    def show_hitory(self):
        # Shows the hitory of perious habits logged
        self.app.clear_screen()

        user = self.app.data[self.app.current_user]

        tk.Label( 
            self.app.root,
            text="Progress History",
            bg="#eef6ea",
            fg="#315d2c",
            font=("Ariel", 26, "bold")
        ).pack(pady=(0, 15))

        tk.Label(
            self.app.root,
            text="Your recent habit logs are saved automatically",
            bg="#eef6ea",
            fg="#315d2c",
            font=("Ariel", 11)
        ).pack(pady=(0, 15))

        list_frame = tk.Frame(
            self.app.root,
            bg="white",
            bd=1,
            relief="solid"
        )
        list_frame.pack(fill="both", expand=True, padx=80, pady=10)

        text = tk.text(
            list_frame,
            font=("consolas", 11),
            bg="white",
            fg="#42583E",
            relief="flat",
            padx=20,
            pady=15
        )
        text.pack(fill="both", expand=True)

        history = user["history"]
        sorted_days = sorted(history.keys(), reverse=True)

        if not sorted_days:
            text.inert("end", "No history yet...")
        else:
            for day in sorted_days[:30]:
                status = history[day]

                if status == "completed":
                    symbol = "✓"
                    word = "Completed"
                elif status == "missed":
                    symbol = "✗"
                    word = "Missed"
                else:
                    symbol = "-"
                    word = "Not Logged"

                text.insert(
                    "end",
                    f"{day:<15} {symbol} {word}\n"
                ) # Displays whether or not a habit was completed in history 

        text.config(state="disabled")

        self.app.make_button(
            self.app.root,
            "Back to your Tree",
            self.app.show_hub,
            20
        ).pack(pady=20)


