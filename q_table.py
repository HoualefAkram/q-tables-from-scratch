from q_value import QValue
from environment import Enviroment
from utils import Utils


class QTable:

    def __init__(self, enviroment: Enviroment):
        self.q_values: list[QValue] = []
        self.enviroment = enviroment
        for action in enviroment.actions:
            for state in enviroment.states:
                q_value: QValue = QValue(state=state, action=action)
                self.q_values.append(q_value)

    def __repr__(self):
        return f"QTable(q_values: {self.q_values})"

    def train(self, iterations: int, learning_rate: float, discount_factor: float):
        for i in range(iterations):
            print(f"iteration: {i}/{iterations}")
            counter = 0
            for q in self.q_values:
                next_state_id = q.state.id + 1

                if next_state_id == len(self.enviroment.states):
                    # last state
                    continue

                next_state_q_vals = [
                    q_val for q_val in self.q_values if q_val.state.id == next_state_id
                ]

                max_next_q = max([q.value for q in next_state_q_vals])

                reward = Utils.get_reward_from_sar(
                    action=q.action, state=q.state, sars=self.enviroment.sars
                )
                new_q_value = q.value + learning_rate * (
                    reward + discount_factor * max_next_q - q.value
                )

                q = q.copyWith(value=new_q_value)
                self.q_values[counter] = q
                counter += 1
