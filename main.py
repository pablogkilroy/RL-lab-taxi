from agent import Agent
from monitor import interact
import gym
import numpy as np

env = gym.make('Taxi-v2')
agent = Agent()
out = env.env.decode(200)
print(list(out))
avg_rewards, best_avg_reward = interact(env, agent)