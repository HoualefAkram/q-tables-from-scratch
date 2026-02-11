from sar import Sar
from state import State
from action import Action
from utils import Utils


class Enviroment:

    def __init__(
        self,
        n_state: int,
        n_action: int,
        rewards: list[float],
        terminal_state_id: int,
    ):

        if n_state * n_action != len(rewards):
            raise Exception("n_state * n_action != len(rewards)")

        self.sars: list[Sar] = []
        self.actions: list[Action] = []
        self.states: list[State] = []
        self.terminal_state_id: int = terminal_state_id

        for s in range(n_state):
            for a in range(n_action):
                reward = rewards[s * n_action + a]
                action = Action(id=a)
                state = State(id=s, is_terminal=s == terminal_state_id)
                sar = Sar(
                    state=state,
                    action=action,
                    reward=reward,
                    next_state=Utils.get_next_state(
                        state=state,
                        action=action,
                        n_state=n_state,
                        terminal_state_id=terminal_state_id,
                    ),
                )
                self.sars.append(sar)

                if state not in self.states:
                    self.states.append(state)

                if action not in self.actions:
                    self.actions.append(action)
