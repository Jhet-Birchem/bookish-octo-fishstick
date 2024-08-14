import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello, World!")

# Set the size of the window
root.geometry("300x200")

# Create a label with "Hello, World!" text
label = tk.Label(root, text="Hello, World!", font=("Arial", 24))
label.pack(pady=20)

# Run the application
root.mainloop()