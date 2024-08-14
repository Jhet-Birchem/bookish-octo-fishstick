import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    # Define standard D&D dice options
    dice_options = {
        "1": 4,
        "2": 6,
        "3": 8,
        "4": 10,
        "5": 12,
        "6": 20
    }
    
    while True:
        # Display options to the user
        print("\nSelect the type of dice to roll:")
        print("1. 4-sided (d4)")
        print("2. 6-sided (d6)")
        print("3. 8-sided (d8)")
        print("4. 10-sided (d10)")
        print("5. 12-sided (d12)")
        print("6. 20-sided (d20)")
        print("7. Quit")

        # Get user input
        choice = input("Enter the number corresponding to your choice: ")

        # Check if the user wants to quit
        if choice == "7":
            print("Goodbye!")
            break

        # Validate and roll the dice
        if choice in dice_options:
            sides = dice_options[choice]
            result = roll_dice(sides)
            print(f"\nYou rolled a {result} on a {sides}-sided die!")
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
