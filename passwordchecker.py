from tkinter import *

def check_password_strength(password):
    # Define rules for password strength
    length_rule = len(password) >= 8
    uppercase_rule = any(c.isupper() for c in password)
    lowercase_rule = any(c.islower() for c in password)
    digit_rule = any(c.isdigit() for c in password)
    special_char_rule = any(c in "!@#$%^&*()-_=+[]{}|;:'<>,.?/" for c in password)

    # Calculate the strength based on rules
    strength = sum([length_rule, uppercase_rule, lowercase_rule, digit_rule, special_char_rule])

    return strength

def update_strength_bar(password):
    strength = check_password_strength(password)
    strength_percentage = strength * 20  # Since there are 5 rules, each contributes 20% to the total strength

    # Update the color of the strength bar based on the percentage
# Update the color of the strength bar based on the percentage
    if strength_percentage < 40:
        color = 'red'
    elif strength_percentage < 60:
        color = 'orange'
    elif strength_percentage < 80:
        color = 'yellow'
    elif strength_percentage < 100:
        color = 'green'  # Hexadecimal color code for bright green
    else:
        color = '#00ff00'  # Hexadecimal color code for bright green


    strength_bar.config(bg=color)
    strength_label.config(text=f"Strength: {strength_percentage}%")

def on_password_change(*args):
    password = password_var.get()
    update_strength_bar(password)

# Create the main window
root = Tk()
root.title("Password Strength Checker")

# Create a password entry field
password_var = StringVar()
password_entry = Entry(root, textvariable=password_var, show='*')
password_entry.pack(pady=10)
password_var.trace_add('write', on_password_change)

# Create a strength bar
strength_bar = Frame(root, width=200, height=20, bg='red')
strength_bar.pack()

# Create a label to display the strength percentage
strength_label = Label(root, text="Strength: 0%", pady=5)
strength_label.pack()

# Start the main loop
root.mainloop()
