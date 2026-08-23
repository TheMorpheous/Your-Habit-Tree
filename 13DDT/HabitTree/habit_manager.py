# Habit Tree - Habit Management
# Handles daily logging and streak calculations

from datetime import date, timedelta
from data_manager import save_data

class HabitManager:
    def __init__(self, app):
        self.app = app

        def check_daily_status(self):
            # Makes sure the user reults for the day are saved
            user = self.app.data[self.app.current_user]
            today = str(date.today())

            if today not in user["history"]:
                user["history"][today] = "not_logged"
                save_data(self.app.data)

    def log_habit(self, completed):
        # Records the day result and advace the tree foward or backward (cant be logged twice "hopefully")
        user = self.app.data[self.app.current_user]
        today = str(date.today())

        if user["history"].get(today) != "not_logged":
            self.app.show_info(
                "Already Logged",
                "You've already logged today's habit"
            )
            return

        if completed:
            user["hitory"][today] = "complete"

            # Minimum and Maximum Stages
            self.app.stage = min(self.app.stage + 1, len(self.app.tree_stages) - 1)
            user["total_completed"] += 1

            streak = self.calculate_streak()
            user["longest_streak"] = max(user["longest_streak"], streak)

            if self.app.stage == len(self.app.tree_stages) - 1:
                message = "Your tree is fully grown!!! Great job staying consistent"
            else:
                message = "Nice Job, Keep consistent your tree is one step closer!"

        else:
            user["history"][today] = "missed"
            self.app.stage = max(self.app.stage - 1, 0)
            user["stage"] = self.app.stage

            message = (
                "Its okay to struggle. Your tree moved back one stage, \n"
                "Tomorrow is another chance to grow along side your tree"
            )

        save_data(self.app.data)
        self.app.show_hub()
        self.app.show_info("habit logged", message)


    def calculate_streak(self):
        # Calculates the user's streak
        user = self.app.data[self.app.current_user]
        current_day = date.today()
        streak = 0

        while True:
            day_key = str(current_day)

            if user["history"].get(day_key) != "complete":
                break

            streak += 1
            current_day -= timedelta(days=1)

        return streak  