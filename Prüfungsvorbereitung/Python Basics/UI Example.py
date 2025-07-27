# Python Basic Input
import tkinter as tk
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello, {name}! You are {age} years old.")

# Basic UI with Tkinter

# Event handling in a simple UI example


def on_button_click(button_id):
    if button_id == 1:
        root.quit()  # Exit the application
    else:
        print(f"Button {button_id} clicked!")


def on_key_press(event):
    print(f"Key pressed: {event.char}")


def on_mouse_click(event):
    print(f"Mouse clicked at: ({event.x}, {event.y})")


# Create the main window
root = tk.Tk()
root.title("Simple UI Example")

# Event Handling Bindings (widget.bind(event, handler))
root.bind("<KeyPress>", on_key_press)  # Bind key press event
root.bind("<Button-1>", on_mouse_click)  # Bind mouse click event

# Create a menu bar
menubar = tk.Menu(root)
menubar.add_command(label="File", command=lambda: print("File menu clicked"))
menubar.add_command(label="Edit", command=lambda: print("Edit menu clicked"))
root.config(menu=menubar)

# Create a label
label = tk.Label(root, text="Welcome to the Simple UI Example!")
label.pack(pady=10)

# Create an entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a listbox
listbox = tk.Listbox(root)
listbox.insert(1, "Item 1")
listbox.insert(2, "Item 2")
listbox.insert(3, "Item 3")
listbox.pack(pady=10)

# Create buttons
button1 = tk.Button(root, text="Exit", command=lambda: on_button_click(1))
button1.pack(pady=10)

# Create a Checkbutton
check_var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Check me!", variable=check_var)
checkbutton.pack(pady=10)

# Create a Radiobutton
radio_var = tk.IntVar()
radiobutton1 = tk.Radiobutton(
    root, text="Option 1", variable=radio_var, value=1)
radiobutton2 = tk.Radiobutton(
    root, text="Option 2", variable=radio_var, value=2)
radiobutton1.pack(pady=5)
radiobutton2.pack(pady=5)

root.mainloop()  # Start the GUI event loop


# Blocking code is Code that prevents the program from continuing until a certain condition is met or an event occurs.
# This can include waiting for user input, file operations, or network requests.
# More to this at Concurrency and Parallelism in Python.
