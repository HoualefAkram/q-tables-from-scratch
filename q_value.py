from typing import Optional


class QValue:

    def __init__(
        self, state_number: int, action_number: int, initial_val: Optional[float] = 0
    ):
        self.state_number: int = state_number
        self.action_number: int = action_number
        self.value: float = initial_val

    def __repr__(self):
        return f"QValue([{self.state_number},{self.action_number}] = {self.value})"

    def __str__(self):
        return f"QValue([{self.state_number},{self.action_number}] = {self.value})"
