from q_value import QValue
from environment import Enviroment


class QTable:

    def __init__(self, enviroment: Enviroment):
        self.q_values: list[QValue] = []
        for action in enviroment.actions:
            for state in enviroment.states:
                q_value: QValue = QValue(state=state, action=action)
                self.q_values.append(q_value)

    def __repr__(self):
        return f"QTable(q_values: {self.q_values})"

    def train(iterations: int, learning_rate: float, discount_factor: float): ...
