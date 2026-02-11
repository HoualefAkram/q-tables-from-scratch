# Q tables from scratch
from q_table import QTable
from environment import Enviroment
from q_value import QValue
from utils import Utils

n_state = 16
n_action = 4  # constant in this example (moving person in a grid)

rewards = [-1 for _ in range(n_action * n_state)]
negative_index = [5, 13, 18, 24, 26, 29, 33, 39, 42, 47, 52, 63]
positive_index = [58, 45]

for n in negative_index:
    rewards[n] = -5

for p in positive_index:
    rewards[p] = 5

terminal_state_id = 15
enviroment = Enviroment(
    n_state=16, n_action=4, rewards=rewards, terminal_state_id=terminal_state_id
)


table = QTable(enviroment=enviroment)

table.train(episodes=1000, learning_rate=0.01, discount_factor=0.9)


# Test
print()
state_id = 4
state = [s for s in enviroment.states if s.id == state_id][0]
while state.id != terminal_state_id:
    qs = []
    # obnoxiously slow, no time to improve it with dicts
    for q in table.q_values:
        if q.state == state:
            qs.append(q)
    best_q: QValue = max(qs, key=lambda x: x.value)
    print(f"current state: {state.id}, action: {best_q.action.description}")
    state = Utils.get_next_state(
        action=best_q.action,
        state=state,
        n_state=n_state,
        terminal_state_id=terminal_state_id,
    )
