from sar import Sar
from state import State
from action import Action


class Enviroment:

    def __init__(
        self,
        n_state: int,
        n_action: int,
        rewards: list[float],
    ):

        if n_state * n_action != len(rewards):
            raise Exception("n_state * n_action != len(rewards)")

        self.sars = []
        self.actions = []
        self.states = []

        for s in range(n_state):
            for a in range(n_action):
                reward = rewards[s * n_action + a]
                state = State(id=s)
                action = Action(id=a)
                sar = Sar(state=state, action=action, reward=reward)
                self.sars.append(sar)

                if state not in self.states:
                    self.states.append(state)

                if action not in self.actions:
                    self.actions.append(action)
