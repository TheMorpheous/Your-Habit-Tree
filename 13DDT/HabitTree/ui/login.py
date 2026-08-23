# Habit Tree - Login UI
# Handles the login and account creation screen


import tkinter as tk

class LoginUI:
    def __init__(self, app):
        self.app = app

    def show_login(self):
        # Displays the loginn screen for the users
        self.app.clear_screen()

        frame = tk.Frame(self.app.root, bg="#eef6ea")
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="HABIT TREE",
            font=("Ariel", 32, "bold"),
            bg="#eef6ea",
            fg="#526b50",
        ).pack(pady=(20, 5))

        tk.Label(
            frame,
            text="Grow your habits. Grow your tree.",
            font=("Arial", 14),
            bg="#eef6ea",
            fg="#526b50",
        ).pack(pady=(0, 25))

        box = tk.Frame(
            frame,
            bg="white",
            bd=1,
            relief="solid",
            padx=30,
            pady=25
        )
        box.pack()

        tk.Label(
            box,
            text="Username",
            bg="white",
            font=("Arial", 11)
        ).pack(anchor="w")

        username_entry = tk.Entry(
            box,
            textvariable=self.app.username_var,
            font=("Arial", 12),
            width=28
        )
        username_entry.pack(pady=(3, 15))

        tk.Label(
            box,
            text="Password",
            bg="white",
            font=("Arial", 11)
        ).pack(anchor="w")

        password_entry = tk.Entry(
            box,
            textvariable=self.app.password_var,
            show="*",
            font=("Arial", 12),
            width=28
        )
        password_entry.pack(pady=(3, 18))

        self.app.make_button(
            box,
            "Login / Create Account",
            self.login,
            25
        ).pack()

        username_entry.focus()

        # Pressing enter will also count like clicking the button
        self.app.root.bind("<Return>", lambda event: self.login())

    def login(self):
        # Log into an already made account or create a new one
        username = self.app.username_var.get().strip()
        password = self.app.password_var.get()

        # Input Validation for username and password
        if not username or not password:
            self.app.show_error(
                "Missing information",
                "Please enter a username or password."
            )
            return

        if len(username) > 20:
            self.app.show_error(
                "Username is too long",
                "Please keep your username under 20 characters."
            )
            return

        if username not in self.app.data:
            # Creating new account 
            from data_manager import make_new_user

            self.app.data[username] = make_new_user(password)
            from data_manager import save_data
            save_data(self.app.data)

            self.app.show_info(
                "Account Created",
                "Your Habit Tree account has been created!!!"
            )

        else:
            # Existing accounts require the same password initially put in
            from data_manager import hash_password

            if self.app.data[username]["password"] != hash_password(password):
                self.app.show_error(
                    "Login has failed",
                    "Wrong password entered."
                )
                return

        self.app.current_user = username
        self.app.stage = self.app.data[username]["stage"]
        self.app.password_var.set("")

        # Checks daily log on enntering main hub
        self.app.habit_manager.check_daily_status()
        self.app.show_hub()