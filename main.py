# Q tables from scratch
from q_table import QTable
from environment import Enviroment

n_state = 16
n_action = 4

rewards = [-1 for _ in range(n_action * n_state)]
negative_index = [5, 13, 18, 24, 26, 29, 33, 39, 42, 47, 52, 63]
positive_index = [58, 45]

for n in negative_index:
    rewards[n] = -5

for p in positive_index:
    rewards[p] = 5


enviroment = Enviroment(n_state=16, n_action=4, rewards=rewards)


table = QTable(enviroment=enviroment)

table.train(iterations=1000, learning_rate=0.01, discount_factor=0.9)

for q in table.q_values:
    if q.state.id == 1:
        print(q)
