# Q tables from scratch
from q_table import QTable
from environment import Enviroment

actions_description = ["Move Left", "Move Down", "Move Right", "Move Up"]

enviroment = Enviroment(n_actions=4, n_states=16, descriptions=actions_description)
table = QTable(enviroment=enviroment)


print(table)
