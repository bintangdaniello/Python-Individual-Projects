# Importing the necessary modules
from tkinter import *
from math import factorial


root = Tk()
root.title('DataFlair - Calculator')
root.geometry("400x500")
root.configure(bg="#A2BBCF")

Label(root, text="Daniel Daniello | 2025-12-05", font=("Arial", 10), bg="#A2BBCF", fg="black").grid(row=0, columnspan=6)

# Constant for pi
PI_VALUE = "3.14"

# It keeps the track of current position on the input text field
i = 0

# Receives the digit as parameter and display it on the input field
def get_variables(num):
    global i
    if display.get() in ["Please enter numbers to calculate!", "Error in calculation!", "Invalid input!"]:
        clear_all()
    display.insert(i, num)
    i = display.index(END)


# Calculate function scans the string to evaluates and display it
def calculate():
    global i
    entire_string = display.get()
    valid_chars = "0123456789.+-*/%^()π²×"
    if any(ch not in valid_chars for ch in entire_string):
        clear_all()
        display.insert(0, "Invalid input!")
        i = 0
        return

    try:
        entire_string = entire_string.replace("π", "*3.14") if not entire_string.startswith("π") else entire_string.replace("π", "3.14", 1).replace("π", "*3.14")
        entire_string = entire_string.replace("²", "**2")
        entire_string = entire_string.replace("^", "**")
        entire_string = entire_string.replace("%", "/100")
        entire_string = entire_string.replace("×", "*")
        a = entire_string
        result = eval(a)
        clear_all()
        display.insert(0, result)
        i = display.index(END)
    except Exception:
        clear_all()
        display.insert(0, "Error in calculation!")
        i = 0


# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    if display.get() in ["Please enter numbers to calculate!", "Error in calculation!", "Invalid input!"]:
        clear_all()
    display.insert(i, operator)
    i = display.index(END)


# Function to clear the input field
def clear_all():
    global i
    display.delete(0, END)
    i = 0


# Function which works like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
        global i
        i = display.index(END)
    else:
        clear_all()
        i = 0


# Function to calculate the factorial and display it
def fact():
    global i
    entire_string = display.get()
    try:
        result = factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
        i = display.index(END)
    except Exception:
        clear_all()
        display.insert(0, "Please enter numbers to calculate!")
        i = display.index(END)


# --------------------------------------UI Design ---------------------------------------------

# adding the input field
display = Entry(root, font=("Helvetica", 18), bg="#A2BBCF", fg="black")
display.grid(row=1, columnspan=6, sticky=N + E + W + S)

# Code to add buttons to the Calculator

Button(root, text="1", command=lambda: get_variables(1), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=2, column=0, sticky=N + S + E + W)
Button(root, text=" 2", command=lambda: get_variables(2), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=2, column=1, sticky=N + S + E + W)
Button(root, text=" 3", command=lambda: get_variables(3), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=2, column=2, sticky=N + S + E + W)

Button(root, text="4", command=lambda: get_variables(4), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=3, column=0, sticky=N + S + E + W)
Button(root, text=" 5", command=lambda: get_variables(5), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=3, column=1, sticky=N + S + E + W)
Button(root, text=" 6", command=lambda: get_variables(6), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=3, column=2, sticky=N + S + E + W)

Button(root, text="7", command=lambda: get_variables(7), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=4, column=0, sticky=N + S + E + W)
Button(root, text=" 8", command=lambda: get_variables(8), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=4, column=1, sticky=N + S + E + W)
Button(root, text=" 9", command=lambda: get_variables(9), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=4, column=2, sticky=N + S + E + W)

# adding other buttons to the calculator
Button(root, text="AC", command=lambda: clear_all(), bg="#FF6347", fg="white", font=("Helvetica", 16)).grid(row=5, column=0, sticky=N + S + E + W)
Button(root, text=" 0", command=lambda: get_variables(0), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=5, column=1, sticky=N + S + E + W)
Button(root, text=" .", command=lambda: get_variables("."), bg="#A2BBCF", fg="black", font=("Helvetica", 16)).grid(row=5, column=2, sticky=N + S + E + W)

Button(root, text="+", command=lambda: get_operation("+"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=2, column=3, sticky=N + S + E + W)
Button(root, text="-", command=lambda: get_operation("-"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=3, column=3, sticky=N + S + E + W)
Button(root, text="×", command=lambda: get_operation("×"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=4, column=3, sticky=N + S + E + W)
Button(root, text="/", command=lambda: get_operation("/"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=5, column=3, sticky=N + S + E + W)

# adding new operations
Button(root, text="π", command=lambda: get_operation("π"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=2, column=4, sticky=N + S + E + W)
Button(root, text="%", command=lambda: get_operation("%"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=3, column=4, sticky=N + S + E + W)
Button(root, text="(", command=lambda: get_operation("("), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=4, column=4, sticky=N + S + E + W)
Button(root, text="^", command=lambda: get_operation("^"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=5, column=4, sticky=N + S + E + W)

Button(root, text="C", command=lambda: undo(), bg="#A9A9A9", fg="white", font=("Helvetica", 16)).grid(row=2, column=5, sticky=N + S + E + W)
Button(root, text="x!", command=lambda: fact(), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=3, column=5, sticky=N + S + E + W)
Button(root, text=")", command=lambda: get_operation(")"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=4, column=5, sticky=N + S + E + W)
Button(root, text="²", command=lambda: get_operation("²"), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(row=5, column=5, sticky=N + S + E + W)
Button(root, text="=", command=lambda: calculate(), bg="#FF9500", fg="white", font=("Helvetica", 16)).grid(columnspan=6, sticky=N + S + E + W)

# Set up 6x6 grid layout so rows and columns expand equally
for x in range(6):
    root.columnconfigure(x, weight=1)
for y in range(6):
    root.rowconfigure(y, weight=1)

root.mainloop()