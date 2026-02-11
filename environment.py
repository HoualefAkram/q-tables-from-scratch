from action import Action
from state import State
from typing import Optional


class Enviroment:

    def __init__(
        self, n_actions: int, n_states: int, descriptions: Optional[list[str]] = None
    ):
        self.actions = []
        self.states = []

        for a in range(n_actions):
            self.actions.append(
                Action(
                    id=a,
                    description=descriptions[a] if descriptions is not None else None,
                )
            )

        for s in range(n_states):
            self.states.append(State(id=s))
