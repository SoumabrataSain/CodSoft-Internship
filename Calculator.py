import tkinter as tk

def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

def clear_display():
    display_var.set("0")

def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception  as e:
        display_var.set("Error")

parent = tk.Tk()
parent.title("Calculator")

display_var = tk.StringVar()
display_var.set("0")

display_label = tk.Label(parent, textvariable=display_var, font=("Arial", 24), anchor="e", bg="lightgray", padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4)

button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for(text, row, col) in button_layout:
    button = tk.Button(parent, text=text, padx=20, pady= 20, font=("Arial", 18),
                       command=lambda t=text: update_display(t) if t != "=" else calculate_result())

    button.grid(row=row, column=col)

clear_button = tk.Button(parent,text="C", padx=20, pady= 20, font=("Arial", 18),command=clear_display)
clear_button.grid(row=5, column=0, columnspan=3)

parent.mainloop()