import tkinter as tk

def click_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for the calculator display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button layout and text
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons in the grid
row = 1
col = 0
for button_text in buttons:
    if button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=calculate)
    elif button_text == 'C':
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=clear_entry)
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=lambda t=button_text: click_button(t))
    
    button.grid(row=row, column=col, sticky="nsew")
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Set up column and row weights to ensure proper resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i + 1, weight=1)

# Start the Tkinter event loop
root.mainloop()
