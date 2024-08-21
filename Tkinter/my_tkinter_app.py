import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Compact Toolbar Design with Functional Buttons")

# Set dark theme background and text colors
dark_bg = "#2E2E2E"
light_text = "#FFFFFF"
entry_bg = "#1E1E1E"
button_color = "#4D4D4D"
button_text_color = "#FFFFFF"
root.configure(bg=dark_bg)

# Function examples for buttons
def log_review():
    print("Log Review clicked!")

def log_entry():
    print("Log Entry clicked!")

def log_in():
    print("Log In clicked!")

def log_out():
    print("Log Out clicked!")

def bg_monitor():
    print("B/G Monitor clicked!")

# Create a frame for the toolbar
toolbar = tk.Frame(root, bg=dark_bg)
toolbar.pack(side="top", fill="x", padx=10, pady=10)

# Add labeled entry fields to the toolbar with default values
fields = [
    ("UTC", ""),
    ("MOC", ""),
    ("MET", "0"),
    ("SLT", "0"),
    ("MJD", "0")
]

for field_text, default_value in fields:
    label = tk.Label(toolbar, text=field_text, bg=dark_bg, fg=light_text, padx=5)
    label.pack(side="left")
    entry = tk.Entry(toolbar, bg=entry_bg, fg=light_text, width=5)
    entry.insert(0, default_value)  # Insert default values like "0"
    entry.pack(side="left", padx=5)

# Add mode dropdown menu with options
mode_label = tk.Label(toolbar, text="Mode", bg=dark_bg, fg=light_text, padx=5)
mode_label.pack(side="left", padx=10)
mode_var = tk.StringVar(value="Choose")
mode_dropdown = ttk.Combobox(toolbar, textvariable=mode_var, values=["Choose", "Option 1", "Option 2"], width=8)
mode_dropdown.pack(side="left", padx=5)

# Add buttons to the toolbar with functionality
buttons = [
    ("Log Review", log_review),
    ("Log Entry", log_entry),
    ("Log In", log_in),
    ("Log Out", log_out),
    ("B/G Monitor", bg_monitor)
]

for button_text, button_command in buttons:
    button = tk.Button(toolbar, text=button_text, bg=button_color, fg=button_text_color, padx=10, command=button_command)
    button.pack(side="left", padx=5)

# Run the Tkinter event loop
root.mainloop()
