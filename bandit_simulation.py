# Project: Implementing Multi-Armed Bandit Algorithms

# Description:
# This script simulates a Multi-Armed Bandit problem and implements multiple strategies:
# - Epsilon-Greedy
# - UCB1 (Upper Confidence Bound)
# - Thompson Sampling
# The goal is to maximize the total reward by choosing the best strategy.

import numpy as np
import matplotlib.pyplot as plt

class BanditArm:
    def __init__(self, true_mean):
        self.true_mean = true_mean
        self.estimated_mean = 0
        self.N = 0

    def pull(self):
        return np.random.randn() + self.true_mean
  
    def update(self, x):
        self.N += 1
        self.estimated_mean = ((self.N - 1) * self.estimated_mean + x) / self.N


class EpsilonGreedy:
    def __init__(self, true_means, epsilon):
        self.epsilon = epsilon
        self.arms = [BanditArm(mu) for mu in true_means]
        self.total_reward = 0
        self.rewards = []

    def select_arm(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(len(self.arms))
        return np.argmax([arm.estimated_mean for arm in self.arms])

    def run(self, iterations):
        for i in range(iterations):
            chosen_arm = self.select_arm()
            reward = self.arms[chosen_arm].pull()
            self.arms[chosen_arm].update(reward)
            self.rewards.append(reward)
            self.total_reward += reward
        return self.rewards


class UCB1:
    def __init__(self, true_means):
        self.arms = [BanditArm(mu) for mu in true_means]
        self.total_reward = 0
        self.rewards = []
        self.time = 0

    def select_arm(self):
        self.time += 1
        ucb_values = []
        for arm in self.arms:
            if arm.N == 0:
                ucb_values.append(float('inf'))
            else:
                bonus = np.sqrt((2 * np.log(self.time)) / arm.N)
                ucb_values.append(arm.estimated_mean + bonus)
        return np.argmax(ucb_values)

    def run(self, iterations):
        for i in range(iterations):
            chosen_arm = self.select_arm()
            reward = self.arms[chosen_arm].pull()
            self.arms[chosen_arm].update(reward)
            self.rewards.append(reward)
            self.total_reward += reward
        return self.rewards


class ThompsonSampling:
    def __init__(self, true_means):
        self.true_means = true_means
        self.alphas = np.ones(len(true_means))
        self.betas = np.ones(len(true_means))
        self.total_reward = 0
        self.rewards = []

    def select_arm(self):
        samples = np.random.beta(self.alphas, self.betas)
        return np.argmax(samples)

    def run(self, iterations):
        for i in range(iterations):
            chosen_arm = self.select_arm()
            reward = np.random.rand() < self.true_means[chosen_arm]
            self.rewards.append(reward)
            self.total_reward += reward
            self.alphas[chosen_arm] += reward
            self.betas[chosen_arm] += 1 - reward
        return self.rewards


# Experiment Setup
true_means = [0.1, 0.5, 0.9]  # True success rates of arms
iterations = 1000

# Running strategies
eps_greedy = EpsilonGreedy(true_means, epsilon=0.1)
ucb1 = UCB1(true_means)
thompson = ThompsonSampling(true_means)

rewards_eps = eps_greedy.run(iterations)
rewards_ucb = ucb1.run(iterations)
rewards_thompson = thompson.run(iterations)

# Plotting Results
plt.figure(figsize=(12, 6))
plt.plot(np.cumsum(rewards_eps), label='Epsilon-Greedy')
plt.plot(np.cumsum(rewards_ucb), label='UCB1')
plt.plot(np.cumsum(rewards_thompson), label='Thompson Sampling')
plt.xlabel("Iterations")
plt.ylabel("Cumulative Reward")
plt.title("Multi-Armed Bandit Strategy Comparison")
plt.legend()
plt.grid()
plt.show()
