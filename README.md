#  Q-Learning Grid World (From Scratch)

A minimal **tabular Q-learning** implementation written from scratch in Python.  
This project demonstrates how a reinforcement learning agent can learn to navigate a grid world toward a terminal goal state using:

- Q-Tables
- Epsilon-Greedy Exploration
- Episodic Training

No external ML or RL libraries are used — everything is implemented manually for educational purposes.

---

## Project Goals

- Understand how Q-learning works internally
- Build an RL agent without frameworks
- Learn episodic training loops
- Implement epsilon-greedy exploration
- Observe reward propagation and policy emergence

---

## Environment

The environment is a square grid where:

- The agent can move:
  - Left
  - Down
  - Right
  - Up
- Illegal moves keep the agent in the same position
- Each action has a reward
- One state is marked as **terminal**
- Episodes end when the terminal state is reached

---

## Learning Algorithm

The agent learns using **Tabular Q-Learning**:

Q(s,a) ← Q(s,a) + α [ r + γ max Q(s',a') − Q(s,a) ]


Where:

- `α` = learning rate
- `γ` = discount factor
- `r` = reward
- `s'` = next state

---

## Exploration Strategy

Epsilon-greedy is used for balancing exploration and exploitation:

- With probability `ε`: choose a random action
- Otherwise: choose the action with highest Q-value

This allows the agent to:

- Explore new paths
- Gradually exploit learned optimal behavior

---

## Project Structure
├── main.py # Entry point & testing loop </br>
├── q_table.py # Training loop & Q-learning logic </br>
├── q_value.py # Q-value representation </br>
├── environment.py # Environment definition </br>
├── state.py # State model </br>
├── action.py # Action model </br>
├── sar.py # Transition representation </br>
└── utils.py # Helper functions </br>



---

## How Training Works

1. A random non-terminal state is selected
2. The agent runs until it reaches the terminal state
3. Each step:
   - Chooses an action using epsilon-greedy
   - Retrieves the transition (SAR)
   - Updates Q-values
4. Episodes repeat for a fixed number of iterations

---

## Running the Project

```bash
python main.py
```

## After training:

- The learned policy is tested
- The agent follows the best Q-values until reaching the terminal state
- Actions are printed step by step

