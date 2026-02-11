from action import Action


class State:

    def __init__(self, id: int):
        self.id = id

    def apply_action(self, action: Action): ...
