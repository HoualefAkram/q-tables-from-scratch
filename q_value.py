from typing import Optional
from state import State
from action import Action


class QValue:

    def __init__(self, state: State, action: Action, initial_val: Optional[float] = 0):
        self.state: State = state
        self.action: Action = action
        self.value: float = initial_val

    def __repr__(self):
        return f"q[{self.state.id},{self.action.id}] = {self.value}\n"

    def __str__(self):
        return f"q[{self.state.id},{self.action.id}] = {self.value}\n"
