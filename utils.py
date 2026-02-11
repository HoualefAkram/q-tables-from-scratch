from action import Action
from state import State
from sar import Sar


class Utils:

    @staticmethod
    def get_reward_from_sar(action: Action, state: State, sars: list[Sar]):
        s = [sar for sar in sars if (sar.state == state and sar.action == action)]
        return s[0].reward
