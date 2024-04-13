# -*- coding: utf-8 -*-
"""RL_lab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K_FtSgAJvSPNKeDtOgtofyt-L_kackvq
"""

import numpy as np

class SARSA:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.Q = np.zeros((n_states, n_actions))
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, self.Q.shape[1])  # explore
        else:
            return np.argmax(self.Q[state, :])  # exploit

    def update(self, state, action, reward, next_state, next_action):
        td_target = reward + self.gamma * self.Q[next_state, next_action]
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.alpha * td_error

# Define environment parameters
n_states = 3  # including start state, intermediate state, and end state
n_actions = 2  # 0 for move left, 1 for move right

# Define the SARSA agent
sarsa_agent = SARSA(n_states, n_actions)

# Define the reward function (assuming it's 0 except at the end state)
def reward_func(state):
    if state == 2:  # end state
        return 1
    else:
        return 0

# Define the main loop for SARSA
num_episodes = 5  # adjust as needed
for episode in range(num_episodes):
    state = 0  # start state
    print(f"Episode {episode + 1}:")
    while state != 2:  # continue until reaching the end state
        action = sarsa_agent.choose_action(state)
        print(f"State: {state}, Action: {action}")
        next_state = max(0, min(state + (action * 2 - 1), n_states - 1))  # move left or right, ensuring next_state remains within bounds
        next_action = sarsa_agent.choose_action(next_state)
        reward = reward_func(next_state)
        print(f"Next State: {next_state}, Next Action: {next_action}, Reward: {reward}")
        sarsa_agent.update(state, action, reward, next_state, next_action)
        state = next_state
    print(f"Reached the end state.")
    print("Q-values:")
    print(sarsa_agent.Q)
    print()

import numpy as np

class QLearning:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.Q = np.zeros((n_states, n_actions))
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate

    def choose_action(self, state, behavior_policy):
        return behavior_policy(state)

    def update(self, state, action, reward, next_state):
        td_target = reward + self.gamma * np.max(self.Q[next_state, :])
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.alpha * td_error

# Define environment parameters
n_states = 3  # including start state, intermediate state, and end state
n_actions = 2  # 0 for move left, 1 for move right

# Define the Q-learning agent
q_learning_agent = QLearning(n_states, n_actions)

# Define the reward function (assuming it's 0 except at the end state)
def reward_func(state):
    if state == 2:  # end state
        return 1
    else:
        return 0

# Define a custom behavior policy
def behavior_policy(state):
    if state == 0:
        return np.random.choice([0, 1])  # Randomly choose an action at the start state
    elif state == 1:
        return 1  # Always choose to move right from the intermediate state
    else:
        return 0  # Always choose to move left from the end state

# Define the main loop for generating episodes with a custom behavior policy
num_episodes = 5  # adjust as needed
episodes = []
for episode in range(num_episodes):
    state = 0  # start state
    episode_steps = []
    while state != 2:  # continue until reaching the end state
        action = q_learning_agent.choose_action(state, behavior_policy)
        next_state = state + (action * 2 - 1)  # move left or right
        reward = reward_func(next_state)
        episode_steps.append((state, action, reward))
        state = next_state
    episodes.append(episode_steps)

# Print the episodes
for i, episode in enumerate(episodes):
    print(f"Episode {i + 1}:")
    for step in episode:
        print(f"State: {step[0]}, Action: {step[1]}, Reward: {step[2]}")
    print()

"""## Qlearning and SARSA When Episodes Given"""

import numpy as np

class SARSA:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.Q = np.zeros((n_states, n_actions))
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, self.Q.shape[1])  # explore
        else:
            return np.argmax(self.Q[state, :])  # exploit

    def update(self, state, action, reward, next_state, next_action):
        td_target = reward + self.gamma * self.Q[next_state, next_action]
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.alpha * td_error

# Define environment parameters
n_states = 3  # including start state, intermediate state, and end state
n_actions = 2  # 0 for move left, 1 for move right

# Define the SARSA agent
sarsa_agent = SARSA(n_states, n_actions)

# Define the main loop for SARSA with given episodes
episodes = [[[0, "R", 10, 1], [1, "L", 1, 0], [0, "R", 15, 1], [1, "R", 35, 2]], [[0, "R", 15, 1], [1, "R", 25, 2]]]

for episode in episodes:
    for step in episode:
        state, action_str, reward, next_state = step
        action = 1 if action_str == "R" else 0  # Convert action string to integer
        next_action = sarsa_agent.choose_action(next_state)
        sarsa_agent.update(state, action, reward, next_state, next_action)

# Print the learned Q-values
print("Q-values:")
print(sarsa_agent.Q)

import numpy as np

class QLearning:
    def __init__(self, n_states, n_actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.Q = np.zeros((n_states, n_actions))
        self.alpha = alpha  # learning rate
        self.gamma = gamma  # discount factor
        self.epsilon = epsilon  # exploration rate

    def choose_action(self, state):
        if np.random.uniform(0, 1) < self.epsilon:
            return np.random.randint(0, self.Q.shape[1])  # explore
        else:
            return np.argmax(self.Q[state, :])  # exploit

    def update(self, state, action, reward, next_state):
        td_target = reward + self.gamma * np.max(self.Q[next_state, :])
        td_error = td_target - self.Q[state, action]
        self.Q[state, action] += self.alpha * td_error

# Define environment parameters
n_states = 3  # including start state, intermediate state, and end state
n_actions = 2  # 0 for move left, 1 for move right

# Define the Q-learning agent
q_learning_agent = QLearning(n_states, n_actions)

# Define the episodes
episodes = [[[0, "R", 10, 1], [1, "L", 1, 0], [0, "R", 15, 1], [1, "R", 35, 2]], [[0, "R", 15, 1], [1, "R", 25, 2]]]

# Define the reward function (assuming it's 0 except at the end state)
def reward_func(state):
    if state == 2:  # end state
        return 1
    else:
        return 0

# Define the main loop for Q-learning with given episodes
for episode in episodes:
    for step in episode:
        state, action_str, reward, next_state = step
        action = 1 if action_str == "R" else 0  # Convert action string to integer
        q_learning_agent.update(state, action, reward, next_state)

# Print the learned Q-values
print("Q-values:")
print(q_learning_agent.Q)

"""## Monte Carlo on Policy and off policy

"""

episodes = [[[0, "R", 10, 1], [1, "L", 1, 0], [0, "R", 15, 1], [1, "R", 35, 2]], [[0, "R", 15, 1], [1, "R", 25, 2]]]

class monte_carlo_on:
    def __init__(self, n, gamma, eps, episodes):
        self.episodes = episodes
        self.n = n
        self.gamma = gamma
        self.eps = eps
        self.q = dict()
        self.policy = dict()
        # self.actions = actions


    def update(self):
        for i in self.episodes:
            returns = 0
            for ind, step in enumerate(i):
                returns = returns + ((self.gamma ** ind) * step[2])
                print(ind, returns)

                if (step[0], step[1]) not in self.q:
                    self.q[(step[0], step[1])] = [returns, 1]

                else:
                    self.q[(step[0], step[1])] = [self.q[(step[0], step[1])][0] + returns, self.q[(step[0], step[1])][1] + 1]

        print(self.q)

        for i in self.q:
            self.q[i] = self.q[i][0] / len(episodes)


        return self.q


    def generate_random_no(self):
        return np.random.uniform(0,1)


    def update_policy(self):
        for i in range(0, self.n-1, 1):
            actions = dict()

            for k in self.q:
                if i == k[0]:
                    if k[1] not in actions:
                        actions[k[1]] = self.q[k]


            greedy_action = None
            soft_action = None
            max_val = float('-inf')

            for act in actions:
                if actions[act] > max_val:
                    max_val = actions[act]
                    greedy_action = act

            rand_no = self.generate_random_no()

            print(rand_no)
            print(list(actions.keys()))


            if rand_no <= self.eps:
                soft_action = random.choice(list(actions.keys()))
            else:
                soft_action = greedy_action

            self.policy[i] = soft_action

        return self.policy

obj = monte_carlo_on(3, 0.1, 0.9, episodes)
obj.update()

class monte_carlo_off:
    def __init__(self, n, actions, gamma, eps, episodes):
        self.episodes = episodes
        self.n = n
        self.actions = ["L","R"]
        self.gamma = gamma
        self.eps = eps
        self.q = dict()
        self.policy = {0:'R', 1:'R'}

        self.c = dict()

        for i in range(0, self.n-1, 1):
            for j in self.actions:
                self.c[(i,j)] = 0

        print(self.c)
        # self.actions = actions


    def find_probability(self,state,action):
        total = 0
        count = 0

        for i in self.episodes:
            for ind,step in enumerate(i):
                if step[0] == state:
                    total += 1

                    if step[1] == action:
                        count += 1

        return count/total


    def update(self):
        # episodes = [[[0, "R", 10, 1], [1, "L", 1, 0], [0, "R", 15, 1], [1, "R", 35, 2]], [[0, "R", 15, 1], [1, "R", 25, 2]]]
        for i in self.episodes:
            returns = 0
            w = 1
            for ind, step in enumerate(i):
                returns = returns + ((self.gamma ** ind) * step[2])
                print(ind, returns)

                self.c[(step[0], step[1])] = self.c[(step[0], step[1])] + w

                if (step[0], step[1]) not in self.q:
                    self.q[(step[0], step[1])] = 0

                self.q[(step[0], step[1])] = self.q[(step[0], step[1])] + ((w /self.c[(step[0], step[1])]) * (returns - self.q[(step[0], step[1])]))

                w = w * (1 / self.find_probability(step[0], step[1]))

                if w == 0:
                    break
                # if (step[0], step[1]) not in self.q:
                #     self.q[(step[0], step[1])] = [returns, 1]

                # else:
                #     self.q[(step[0], step[1])] = [self.q[(step[0], step[1])][0] + returns, self.q[(step[0], step[1])][1] + 1]

        print(self.q)

        # for i in self.q:
        #     self.q[i] = self.q[i] / len(episodes)


        return self.q


    def generate_random_no(self):
        return np.random.uniform(0,1)

    # def update_policy(self):
    #     for i in range(0, self.n-1, 1):
    #         actions = dict()

    #         for k in self.q:
    #             if i == k[0]:
    #                 if k[1] not in actions:
    #                     actions[k[1]] = self.q[k]


    #         greedy_action = None
    #         soft_action = None
    #         max_val = float('-inf')

    #         for act in actions:
    #             if actions[act] > max_val:
    #                 max_val = actions[act]
    #                 greedy_action = act

    #         rand_no = self.generate_random_no()

    #         print(rand_no)
    #         print(list(actions.keys()))


    #         if rand_no <= self.eps:
    #             soft_action = random.choice(list(actions.keys()))
    #         else:
    #             soft_action = greedy_action

    #         self.policy[i] = soft_action

    #     return self.policy

obj = monte_carlo_off(3, [], 0.1, 0.9, episodes)
obj.update()

"""## MC Extra"""

import numpy as np

class MonteCarloOnPolicy:
    def __init__(self, n_states, n_actions, gamma, epsilon, episodes):
        self.n_states = n_states
        self.n_actions = n_actions
        self.gamma = gamma
        self.epsilon = epsilon
        self.episodes = episodes
        self.Q = np.zeros((n_states, n_actions))
        self.returns_sum = np.zeros((n_states, n_actions))
        self.returns_count = np.zeros((n_states, n_actions))
        self.policy = np.random.randint(0, n_actions, size=n_states)

    def generate_random_number(self):
        return np.random.uniform(0, 1)

    def update_policy(self):
        for episode in self.episodes:
            G = 0
            visited_states_actions = []
            for state, action_str, reward, _ in episode:
                action = 1 if action_str == "R" else 0
                visited_states_actions.append((state, action))
                G = self.gamma * G + reward

            for state, action in visited_states_actions:
                index = state, action
                self.returns_sum[index] += G
                self.returns_count[index] += 1
                self.Q[state, action] = self.returns_sum[index] / self.returns_count[index]

            for state in range(self.n_states):
                self.policy[state] = np.argmax(self.Q[state, :])

    def update(self):
        for _ in range(self.n_states):
            rand_num = self.generate_random_number()
            if rand_num <= self.epsilon:
                self.policy[_] = np.random.randint(0, self.n_actions)
            else:
                self.policy[_] = np.argmax(self.Q[_, :])

    def print_q_values(self):
        print("Q-values:")
        for state in range(self.n_states):
            for action in range(self.n_actions):
                print(f"State: {state}, Action: {action}, Q-value: {self.Q[state, action]}")

    def print_value_function(self):
        print("Value function:")
        for state in range(self.n_states):
            print(f"State: {state}, Value: {np.max(self.Q[state, :])}")

# Define environment parameters
n_states = 3  # including start state, intermediate state, and end state
n_actions = 2  # 0 for move left, 1 for move right
gamma = 1.0  # discount factor
epsilon = 0.1  # exploration rate

# Define the episodes
episodes = [
    [[0, "R", 10, 1], [1, "L", 1, 0], [0, "R", 15, 1], [1, "R", 35, 2]],
    [[0, "R", 15, 1], [1, "R", 25, 2]]
]

# Initialize and run Monte Carlo on-policy algorithm
monte_carlo_on_policy = MonteCarloOnPolicy(n_states, n_actions, gamma, epsilon, episodes)
monte_carlo_on_policy.update_policy()

# Print Q-values and value function
monte_carlo_on_policy.print_q_values()
monte_carlo_on_policy.print_value_function()

import numpy as np

def generate_episode(policy):
    episode = []
    state = 0  # Assuming starting state is always 0
    while True:
        action = np.random.choice(policy[state])
        next_state = state + action
        reward = 0  # Assuming no rewards until the goal state
        episode.append((state, action, reward, next_state))
        state = next_state
        if state == 2:  # Assuming state 2 is the goal state
            break
    return episode

def monte_carlo_on_policy(episodes, gamma=1.0):
    returns_sum = {}
    returns_count = {}
    Q = {}

    for episode in episodes:
        states_actions_visited = set()
        G = 0
        for t in range(len(episode)):
            state, action, reward, next_state = episode[t]
            sa_pair = (state, action)
            G = gamma * G + reward

            if not sa_pair in states_actions_visited:
                if sa_pair in returns_sum:
                    returns_sum[sa_pair] += G
                    returns_count[sa_pair] += 1
                else:
                    returns_sum[sa_pair] = G
                    returns_count[sa_pair] = 1
                Q[sa_pair] = returns_sum[sa_pair] / returns_count[sa_pair]
                states_actions_visited.add(sa_pair)

    return Q

def e_greedy_policy(Q, state, epsilon):
    if np.random.random() < epsilon:
        return np.random.choice([-1, 1])  # Assuming actions are either -1 (Left) or 1 (Right)
    else:
        return np.argmax([Q.get((state, a), 0) for a in [-1, 1]])

def monte_carlo_control(episodes, num_episodes, epsilon, gamma=1.0):
    Q = {}
    N = {}
    policy = {}

    for episode in range(num_episodes):
        episode_states_actions = []
        episode_rewards = []
        state = 0  # Assuming starting state is always 0
        while True:
            action = e_greedy_policy(Q, state, epsilon)
            episode_states_actions.append((state, action))
            next_state = state + action
            reward = 0  # Assuming no rewards until the goal state
            episode_rewards.append(reward)
            state = next_state
            if state == 2:  # Assuming state 2 is the goal state
                break

        G = 0
        for t in range(len(episode_states_actions) - 1, -1, -1):
            state, action = episode_states_actions[t]
            sa_pair = (state, action)
            G = gamma * G + episode_rewards[t]

            if not sa_pair in [(s, a) for s, a in episode_states_actions[:t]]:
                if sa_pair in N:
                    N[sa_pair] += 1
                else:
                    N[sa_pair] = 1
                if sa_pair in Q:
                    Q[sa_pair] += (G - Q[sa_pair]) / N[sa_pair]
                else:
                    Q[sa_pair] = G / N[sa_pair]
                policy[state] = [np.argmax([Q.get((state, a), 0) for a in [-1, 1]])]

    return Q, policy

# Given episodes
episodes = [[[0, "R", 10, 1], [1, "L", 1, 0], [0, "R", 15, 1], [1, "R", 35, 2]], [[0, "R", 15, 1], [1, "R", 25, 2]]]

# Monte Carlo on-policy evaluation
Q_values_evaluation = monte_carlo_on_policy(episodes)
print("Q-values after evaluation:")
for k, v in Q_values_evaluation.items():
    print(k, v)

# Monte Carlo control
num_episodes = 1000
epsilon = 0.1
Q_values_control, policy_control = monte_carlo_control(episodes, num_episodes, epsilon)
print("\nQ-values after control:")
for k, v in Q_values_control.items():
    print(k, v)
print("\nPolicy after control:", policy_control)

import numpy as np

def generate_episode(policy):
    episode = []
    state = 0  # Assuming starting state is always 0
    while True:
        action = np.random.choice(policy[state])
        next_state = state + action
        reward = 0  # Assuming no rewards until the goal state
        episode.append((state, action, reward, next_state))
        state = next_state
        if state == 2:  # Assuming state 2 is the goal state
            break
    return episode

def monte_carlo_policy_evaluation(episodes, gamma=1.0):
    returns_sum = {}
    returns_count = {}
    V = {}

    for episode in episodes:
        G = 0
        for t in range(len(episode)):
            state, _, reward, _ = episode[t]
            G = gamma * G + reward

            if state not in [ep[0] for ep in episode[:t]]:
                if state in returns_sum:
                    returns_sum[state] += G
                    returns_count[state] += 1
                else:
                    returns_sum[state] = G
                    returns_count[state] = 1
                V[state] = returns_sum[state] / returns_count[state]

    return V

def e_greedy_policy(Q, state, epsilon):
    if np.random.random() < epsilon:
        return np.random.choice([-1, 1])  # Assuming actions are either -1 (Left) or 1 (Right)
    else:
        return np.argmax([Q.get((state, a), 0) for a in [-1, 1]])

def monte_carlo_policy_control(episodes, num_episodes, epsilon, gamma=1.0):
    Q = {}
    N = {}
    policy = {}

    for episode in range(num_episodes):
        episode_states_actions = []
        episode_rewards = []
        state = 0  # Assuming starting state is always 0
        while True:
            action = e_greedy_policy(Q, state, epsilon)
            episode_states_actions.append((state, action))
            next_state = state + action
            reward = 0  # Assuming no rewards until the goal state
            episode_rewards.append(reward)
            state = next_state
            if state == 2:  # Assuming state 2 is the goal state
                break

        G = 0
        for t in range(len(episode_states_actions) - 1, -1, -1):
            state, action = episode_states_actions[t]
            sa_pair = (state, action)
            G = gamma * G + episode_rewards[t]

            if not sa_pair in [(s, a) for s, a in episode_states_actions[:t]]:
                if sa_pair in N:
                    N[sa_pair] += 1
                else:
                    N[sa_pair] = 1
                if sa_pair in Q:
                    Q[sa_pair] += (G - Q[sa_pair]) / N