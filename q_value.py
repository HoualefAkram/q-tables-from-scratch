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

    def set_value(self, new_value: float):
        self.value = new_value

    def copyWith(
        self,
        state: Optional[State] = None,
        action: Optional[Action] = None,
        value: Optional[float] = None,
    ):
        return QValue(
            action=action if action != None else self.action,
            state=state if state != None else self.state,
            initial_val=value if value != None else self.value,
        )
