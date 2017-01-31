import gym
from gym import spaces

env = gym.make('CartPole-v0')
#print(env.action_space)
obs = env.observation_space
print(obs[0])
print(env.observation_space.high)
print(env.observation_space.low)

space = spaces.Discrete(8)
x = space.sample()


assert space.contains(x)
assert space.n==8

