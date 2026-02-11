from action import Action
from typing import Callable


class State:
    def __init__(self, id: int):
        self.id = id

    def on_action(self, action: Action, func: Callable[[Action], int]):
        self.id = func(action)
