# Startpunkt der Anwendung
from controller import CalculatorController
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    root.title("MVC Rechner mit Tkinter")
    app = CalculatorController(root)
    root.mainloop()
