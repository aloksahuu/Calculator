import tkinter as tk
from tkinter import ttk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    selected_operation = combo_operation.get()

    if selected_operation == 'Addition':
        result = add(num1, num2)
    elif selected_operation == 'Subtraction':
        result = subtract(num1, num2)
    elif selected_operation == 'Multiplication':
        result = multiply(num1, num2)
    elif selected_operation == 'Division':
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    result_label.config(text=f"Result: {result}")

# Create the main application window
app = tk.Tk()
app.title("Simple Calculator App")

# Create widgets
label_num1 = tk.Label(app, text="Enter first number:")
entry_num1 = ttk.Entry(app)

label_num2 = tk.Label(app, text="Enter second number:")
entry_num2 = ttk.Entry(app)

label_operation = tk.Label(app, text="Select operation:")
operations = ['Addition', 'Subtraction', 'Multiplication', 'Division']
combo_operation = ttk.Combobox(app, values=operations)

calculate_button = ttk.Button(app, text="Calculate", command=calculate)
result_label = tk.Label(app, text="Result:")

# Place widgets in the window
label_num1.pack()
entry_num1.pack()

label_num2.pack()
entry_num2.pack()

label_operation.pack()
combo_operation.pack()

calculate_button.pack()

result_label.pack()

# Start the main event loop
app.mainloop()

