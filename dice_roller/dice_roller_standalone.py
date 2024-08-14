import tkinter as tk
import random

# Function to roll the dice
def roll_dice():
    sides = int(dice_var.get())  # Get the selected number of sides
    result = random.randint(1, sides)
    result_label.config(text=f"You rolled a {result}!")

# Create the main window
root = tk.Tk()
root.title("Dice Roller")

# Set the size of the window
root.geometry("400x250")

# Create a label to instruct the user
instruction_label = tk.Label(root, text="Select dice type and click 'Roll' to roll the dice", font=("Arial", 14))
instruction_label.pack(pady=10)

# Create a dropdown menu for selecting dice type
dice_var = tk.StringVar(root)
dice_var.set("6")  # Set default dice to 6-sided

dice_options = ["4", "6", "8", "10", "12", "20"]  # D&D standard dice
dice_menu = tk.OptionMenu(root, dice_var, *dice_options)
dice_menu.config(font=("Arial", 14))
dice_menu.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Click 'Roll' to roll the dice", font=("Arial", 18))
result_label.pack(pady=20)

# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll", font=("Arial", 18), command=roll_dice)
roll_button.pack(pady=20)

# Run the application
root.mainloop()