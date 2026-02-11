from state import State
from action import Action


class Sar:
    def __init__(self, state: State, action: Action, reward: float):
        self.state: State = state
        self.action: Action = action
        self.reward: float = reward

    def __repr__(self):
        return f"Sar(state_id: {self.state.id}, action_id: {self.action.id}, reward: {self.reward})"
