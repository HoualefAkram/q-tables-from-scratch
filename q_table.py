from q_value import QValue
from environment import Enviroment
from utils import Utils
from random import choice


class QTable:

    def __init__(self, enviroment: Enviroment):
        self.q_values: list[QValue] = []
        self.enviroment = enviroment
        for state in enviroment.states:
            for action in enviroment.actions:
                q_value: QValue = QValue(state=state, action=action)
                self.q_values.append(q_value)

    def __repr__(self):
        return f"QTable(q_values: {self.q_values})"

    def train(self, episodes: int, learning_rate: float, discount_factor: float):
        for episode in range(episodes):
            print(f"Episode {episode}/{episodes}")
            run = True
            current_state = choice(self.enviroment.states)  # start point

            steps = 0  # safety in case of an infinite loop
            max_steps = 400

            while run:
                random_action = choice(self.enviroment.actions)
                sar = Utils.get_sar(
                    action=random_action,
                    state=current_state,
                    sars=self.enviroment.sars,
                )
                next_state = sar.next_state
                max_q_next_state = max(
                    [j.value for j in self.q_values if j.state == next_state]
                )
                reward = sar.reward

                current_q = [
                    q
                    for q in self.q_values
                    if (q.state == current_state and q.action == random_action)
                ][0]
                q_val = current_q.value + learning_rate * (
                    reward + discount_factor * max_q_next_state - current_q.value
                )
                current_q.set_value(new_value=q_val)

                if next_state.is_terminal:
                    run = False
                    continue

                current_state = next_state
                steps += 1
                if steps >= max_steps:
                    break
