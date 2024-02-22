import tkinter as tk
import sqlite3

def add_debt():
    name = name_entry.get()
    debt = float(debt_entry.get())
    # Insert the debt into the database
    cursor.execute("INSERT INTO debts (name, debt) VALUES (?, ?)", (name, debt))
    connection.commit()
    update_display()

def update_display():
    # Retrieve debts from the database
    cursor.execute("SELECT name, debt FROM debts")
    debt_data = cursor.fetchall()
    display_text.set("\n".join([f"{name}: ${debt}" for name, debt in debt_data]))

# Connect to the SQLite database (creates a new database if it doesn't exist)
connection = sqlite3.connect("debts.db")
cursor = connection.cursor()

# Create a table to store debts if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS debts (name TEXT, debt REAL)")

# Create the main application window
root = tk.Tk()
root.title("Debt Tracker")

# Create and place widgets
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Debt:").grid(row=1, column=0)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

debt_entry = tk.Entry(root)
debt_entry.grid(row=1, column=1)

add_button = tk.Button(root, text="Add Debt", command=add_debt)
add_button.grid(row=2, column=0, columnspan=2)

display_text = tk.StringVar()
display_label = tk.Label(root, textvariable=display_text)
display_label.grid(row=3, column=0, columnspan=2)

# Run the application
root.mainloop()

# Close the database connection when the application is closed
connection.close()