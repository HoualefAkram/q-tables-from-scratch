from typing import Optional
from sar import Sar
from state import State


class Enviroment:

    def __init__(
        self,
        states_actions_rewards: list[Sar],
    ):
        self.states = []
        self.actions = []
        self.terminal_states: list[State] = []

        for i in states_actions_rewards:
            state = i.state
            action = i.action
            if state not in self.states:
                self.states.append(state)
                if state.is_terminal:
                    self.terminal_states.append(state)
            if action not in self.actions:
                self.actions.append(action)
