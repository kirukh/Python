# Template für die UI-Darstellung
import tkinter as tk


class CalculatorView(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label1 = tk.Label(self, text="Zahl 1:")
        self.label1.grid(row=0, column=0)

        self.entry1 = tk.Entry(self)
        self.entry1.grid(row=0, column=1)

        self.label2 = tk.Label(self, text="Zahl 2:")
        self.label2.grid(row=1, column=0)

        self.entry2 = tk.Entry(self)
        self.entry2.grid(row=1, column=1)

        self.button = tk.Button(self, text="Addieren",
                                command=self.controller.on_add)
        self.button.grid(row=2, column=0, columnspan=2)

        self.result_label = tk.Label(self, text="Ergebnis:")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def get_input(self):
        return self.entry1.get(), self.entry2.get()

    def show_result(self, result):
        self.result_label.config(text=f"Ergebnis: {result}")
