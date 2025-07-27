# Controller für Benutzeroperationen
from view import CalculatorView
from model import CalculatorModel


class CalculatorController:
    def __init__(self, root):
        self.model = CalculatorModel()
        self.view = CalculatorView(root, self)

    def on_add(self):
        a, b = self.view.get_input()
        result = self.model.add(a, b)
        self.view.show_result(result)
