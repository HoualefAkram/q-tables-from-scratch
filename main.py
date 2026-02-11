# Q tables from scratch
from q_table import QTable
from environment import Enviroment
from sar import Sar
from state import State
from action import Action

actions_description = ["Move Left", "Move Down", "Move Right", "Move Up"]


sars = [
    # state 1
    Sar(state=State(id=0, is_terminal=False), action=Action(id=0), reward=0),
    Sar(state=State(id=0, is_terminal=False), action=Action(id=1), reward=0),
    Sar(state=State(id=0, is_terminal=False), action=Action(id=2), reward=0),
    Sar(state=State(id=0, is_terminal=False), action=Action(id=3), reward=0),
    # state 2
    Sar(state=State(id=1, is_terminal=False), action=Action(id=0), reward=0),
    Sar(state=State(id=1, is_terminal=False), action=Action(id=1), reward=0),
    Sar(state=State(id=1, is_terminal=False), action=Action(id=2), reward=0),
    Sar(state=State(id=1, is_terminal=False), action=Action(id=3), reward=0),
    # state 3
    Sar(
        state=State(id=2, is_terminal=False, is_negative=True),
        action=Action(id=0),
        reward=0,
    ),
    Sar(
        state=State(id=2, is_terminal=False, is_negative=True),
        action=Action(id=1),
        reward=0,
    ),
    Sar(
        state=State(id=2, is_terminal=False, is_negative=True),
        action=Action(id=2),
        reward=0,
    ),
    Sar(
        state=State(id=2, is_terminal=False, is_negative=True),
        action=Action(id=3),
        reward=1,
    ),
    # state 4
    Sar(state=State(id=3, is_terminal=True), action=Action(id=0), reward=0),
    Sar(state=State(id=3, is_terminal=True), action=Action(id=1), reward=0),
    Sar(state=State(id=3, is_terminal=True), action=Action(id=2), reward=0),
    Sar(state=State(id=3, is_terminal=True), action=Action(id=3), reward=0),
    # state 5
    Sar(state=State(id=4, is_terminal=False), action=Action(id=0), reward=0),
    Sar(state=State(id=4, is_terminal=False), action=Action(id=1), reward=0),
    Sar(state=State(id=4, is_terminal=False), action=Action(id=2), reward=0),
    Sar(state=State(id=4, is_terminal=False), action=Action(id=3), reward=0),
]

enviroment = Enviroment(states_actions_rewards=sars)


table = QTable(enviroment=enviroment)


print(table)

print(enviroment.actions)
print(enviroment.states)
