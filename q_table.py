from q_value import QValue


class QTable:

    def __init__(self, n_actions: int, n_states: int):
        self.q_values: list[QValue] = []
        for action in range(n_actions):
            for state in range(n_states):
                q_value: QValue = QValue(state_number=state, action_number=action)
                self.q_values.append(q_value)

    def __repr__(self):
        return f"QTable(q_values: {self.q_values})"

    def train(iterations: int, learning_rate: float, discount_factor: float): ...
