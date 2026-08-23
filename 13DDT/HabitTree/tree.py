# Habit Tree - Tree Drawing
# Contains the visual tree and stage information

import tkinter as tk


# Tree growing from small to big
TREE_STAGES = [
    "Seed",
    "Sprout",
    "Young Tree",
    "Growing Tree",
    "Strong Tree",
    "Big Tree",
    "Fully Grown"
]


# Cool quotes found from Internet (:
STAGE_DESCRIPTIONS = [
    "Every tree starts somewhere.",
    "Your first little signs of growth!",
    "The habit is starting to take root.",
    "Your consistency is showing.",
    "Your tree is getting stronger.",
    "Look how much you have grown.",
    "Fully grown! Keep looking after it."
]


def draw_tree(canvas, stage):
    # Makes the tree
    canvas.delete("all")

    # The ground
    canvas.create_oval(80, 350, 570, 405, fill="#8fbd7e", outline="")

    # Tree trunk size
    trunk_height = 50 + stage * 32
    bottom_y = 355
    top_y = bottom_y - trunk_height

    canvas.create_rectangle(
        305, top_y, 350, bottom_y,
        fill="#765331",
        outline="#412915"
    )

    # Branches 
    if stage >= 2:
        canvas.create_line(
            325, top_y + 80, 260, top_y + 35,
            width=10, fill="#765331"
        )
        canvas.create_line(
            330, top_y + 110, 395, top_y + 55,
             width=10, fill="#765331"
        )

    # Different stage = different size leaves
    if stage == 0:
        canvas.create_oval(
            315, top_y - 20, 340, top_y + 5,
            fill="#4f9250", 
            outline=""
        )

    elif stage == 1:
        canvas.create_oval(
            275, top_y - 15, 360, top_y + 65,
            fill="#4f9250", 
            outline=""
        )

    else:
        radius = 65 + stage * 7

        #Creates 3 ovals a main bush
        canvas.create_oval(
            325 - radius, top_y - radius,
            325 + radius, top_y + radius,
            fill="#4f9250", 
            outline=""
        )   

        canvas.create_oval(
            270 - radius // 2, top_y - 20,
            270 + radius // 2, top_y + radius + 40,
            fill="#66a65a",
            outline=""
        )  

        canvas.create_oval(
            385 - radius // 2, top_y - 30,
            385 + radius // 2, top_y + radius + 35,
            fill="#5b9e53",
            outline=""
        ) 

    # Fruit appears at final stage
    if stage >= 5:
        fruit_positions = [
            (275, top_y + 30),
            (365, top_y + 55),
            (315, top_y - 5),
            (405, top_y + 10)
        ]

        for x, y in fruit_positions:
            canvas.create_oval(
                x - 7, y - 7, x + 7, y + 7,
                fill="#d48b7c",
                outline=""
            )

    # Flowers when fully grown
    if stage == len(TREE_STAGES) - 1:
        for x, y in [
            (250, top_y + 20),
            (390, top_y + 25),
            (325, top_y - 20)
        ]:
            canvas.create_text(
                x, y, 
                text="",
                font=("Ariel", 20),
                fill="#f2a6bd"
            )
