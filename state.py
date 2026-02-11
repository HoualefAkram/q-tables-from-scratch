from action import Action
from typing import Callable, Optional


class State:
    def __init__(self, id: int):
        self.id = id

    def on_action(self, action: Action, func: Callable[[Action], int]) -> int:
        return func(action)

    def copyWith(
        self,
        id: Optional[int] = None,
        is_terminal: Optional[bool] = None,
        is_negative: Optional[bool] = None,
    ):
        return State(
            id=id if id is not None else self.id,
            is_terminal=is_terminal if is_terminal is not None else self.is_terminal,
            is_negative=is_negative if is_negative is not None else self.is_negative,
        )

    def __repr__(self):
        return f"State(id: {self.id})"

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
