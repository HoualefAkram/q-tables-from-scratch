# Q tables from scratch
from q_table import QTable
from environment import Enviroment
from sar import Sar
from state import State
from action import Action

n_state = 16
n_action = 4

rewards = [0 for _ in range(n_action * n_state)]
negative_index = [5, 13, 18, 24, 26, 29, 33, 39, 42, 47, 52, 63]
positive_index = [58, 45]

for n in negative_index:
    rewards[n] = -1

for p in positive_index:
    rewards[p] = 1


enviroment = Enviroment(n_state=16, n_action=4, rewards=rewards)


table = QTable(enviroment=enviroment)


print(table)
