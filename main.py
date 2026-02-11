# Q tables from scratch
from q_table import QTable
from environment import Enviroment

enviroment = Enviroment(n_actions=4, n_states=4)
table = QTable(enviroment=enviroment)

print(table)
