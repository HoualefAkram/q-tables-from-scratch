from state import State
from action import Action


class Sar:
    def __init__(self, state: State, action: Action, reward: float, next_state: State):
        self.state: State = state
        self.action: Action = action
        self.next_state: State = next_state
        self.reward: float = reward

    def __repr__(self):
        return f"Sar(state_id: {self.state.id}, action_id: {self.action.id}, reward: {self.reward}, next_state_id: {self.next_state.id})"
