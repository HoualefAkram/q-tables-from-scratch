from action import Action
from typing import Callable, Optional


class State:
    def __init__(self, id: int, is_terminal: bool):
        self.id = id
        self.is_terminal = is_terminal

    def copyWith(
        self,
        id: Optional[int] = None,
        is_terminal: Optional[bool] = None,
    ):
        return State(
            id=id if id is not None else self.id,
            is_terminal=is_terminal if is_terminal is not None else self.is_terminal,
        )

    def __repr__(self):
        return f"State(id: {self.id})"

    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
