# Habit Tree - Data Management
# Handles loading, saving, password hashing, and creating new users

import json
import os
import hashlib


# Saves the data into a JSON file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "habit_tree_data.json")

def hash_password(password):
    # Turns the a random value that is stored locally
    if not os.path.exists(DATA_FILE):
        return[]


def load_save():
    # Loads the saved data for user
    if not os.path.exists(DATA_FILE):
        return[]

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return jon.load(file)
    except (json.JSONDecodeError, OSError):
        return[] # Start safey if save file is unnreadable


def save_data(data):
    # Saves the ussers info
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def make_new_user(password):
    # Creates default info for new users
    return{
        "password": hash_password(password),
        "stage": 0,
        "history": {},
        "longest_streak": 0,
        "total_completed": 0,
    }
