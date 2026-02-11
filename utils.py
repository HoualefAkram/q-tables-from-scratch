from action import Action
from state import State
from sar import Sar
from math import sqrt


class Utils:

    @staticmethod
    def get_sar(action: Action, state: State, sars: list[Sar]) -> Sar:
        s = [sar for sar in sars if (sar.state == state and sar.action == action)]
        return s[0]

        # Assume the grid is a square

    @staticmethod
    def get_next_state(
        state: State, action: Action, n_state: int, terminal_state_id: int
    ):
        side_len = int(sqrt(n_state))
        top = [i for i in range(side_len)]
        left = [i for i in range(0, n_state, side_len)]
        right = [i for i in range(side_len - 1, n_state, side_len)]
        bottom = [i for i in range(n_state - side_len, n_state)]

        # illegal move = stay on the same state
        if state.id in top and action.id == 3:
            return state
        if state.id in left and action.id == 0:
            return state
        if state.id in right and action.id == 2:
            return state
        if state.id in bottom and action.id == 1:
            return state

        # legal moves
        if action.id == 0:  # left (-1)
            new_id = state.id - 1
        if action.id == 1:  # down (+ side len)
            new_id = state.id + side_len
        if action.id == 2:  # right (+1)
            new_id = state.id + 1
        if action.id == 3:  # up (- side len)
            new_id = state.id - side_len

        return state.copyWith(id=new_id, is_terminal=new_id == terminal_state_id)
