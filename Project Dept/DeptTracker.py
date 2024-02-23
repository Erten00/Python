import tkinter as tk
import sqlite3

class CustomTkinter:
    def __init__(self, master=None):
        self.master = master

    def Label(self, text='', **kwargs):
        label = tk.Label(self.master, text=text, **kwargs)
        label.pack()
        return label

    def Entry(self, **kwargs):
        entry = tk.Entry(self.master, **kwargs)
        entry.pack()
        return entry

    def Button(self, text='', command=None, **kwargs):
        button = tk.Button(self.master, text=text, command=command, **kwargs)
        button.pack()
        return button

    def OptionMenu(self, options, **kwargs):
        option_var = tk.StringVar(self.master)
        option_var.set(options[0])
        option_menu = tk.OptionMenu(self.master, option_var, *options)
        option_menu.pack()
        return option_var

# Create a custom Tkinter-like library instance
ctk = CustomTkinter()

# Create the main application window
root = tk.Tk()
root.title("Debt Tracker")

# Set fullscreen
root.attributes('-fullscreen', True)

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position for centered window
x_position = (screen_width - root.winfo_reqwidth()) / 2
y_position = (screen_height - root.winfo_reqheight()) / 2

# Set geometry to center window
root.geometry("+%d+%d" % (x_position, y_position))

# Connect to the SQLite database
connection = sqlite3.connect("debts.db")
cursor = connection.cursor()

# Create and place widgets
ctk.Label(text="Debtor:")
ctk.Label(text="Creditor:")
ctk.Label(text="Debt:")

# Pre-specified debtor name
debtor_options = ["John", "Jane", "Alice"]  # Add your list of debtor names here
debtor_var = ctk.OptionMenu(options=debtor_options)

creditor_entry = ctk.Entry()
debt_entry = ctk.Entry()

def add_debt():
    debtor = debtor_var.get()
    creditor = creditor_entry.get()
    debt = float(debt_entry.get())
    insert_debt(debtor, creditor, debt)  # Call the function to insert debt into the database
    update_display()

def insert_debt(debtor, creditor, debt):
    # Insert the debt into the database
    cursor.execute("INSERT INTO debts (debtor, creditor, debt) VALUES (?, ?, ?)", (debtor, creditor, debt))
    connection.commit()

def update_display():
    # Retrieve debts from the database
    cursor.execute("SELECT debtor, creditor, debt FROM debts")
    debt_data = cursor.fetchall()
    display_text.set("\n".join([f"{debtor} owes {creditor}: ${debt}" for debtor, creditor, debt in debt_data]))

ctk.Button(text="Add Debt", command=add_debt)

display_text = tk.StringVar()
display_label = ctk.Label(textvariable=display_text)
display_label.pack()

# Run the application
root.mainloop()

# Close the database connection when the application is closed
connection.close()