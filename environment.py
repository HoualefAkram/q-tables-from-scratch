from typing import Optional
from sar import Sar


class Enviroment:

    def __init__(
        self,
        states_actions_rewards: list[Sar],
        actions_description: Optional[list[str]] = None,
    ):
        self.states = []
        self.actions = []

        for i in states_actions_rewards:
            state = i.state
            action = i.action
            if state not in self.states:
                self.states.append(state)
            if action not in self.actions:
                self.actions.append(action)
