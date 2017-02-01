import gym
from gym import monitoring
from gym import Wrapper
import random
import numpy as np
from collections import defaultdict


#q = defaultdict(lambda:0)

def state(observation):
	if(observation[2] <= -0.26):
		i = 0
	elif(observation[2] <= -0.13):
		i = 1
	elif(observation[2] <= 0):
		i = 2
	elif(observation[2] <= 0.13):
		i = 3
	elif(observation[2] <= 0.26):
		i = 4
	else:
		i = 5

	return i



def choose_action(state, epsilon):
	if random.random() < epsilon:
		action = env.action_space.sample()

	else:
		print q_table[state]
		action = np.argmax(q_table[state])
	return action


env = gym.make('CartPole-v0')

#env = wrappers.Monitor(env,temp)

q_table = np.zeros((6,2))


num_streaks = 0
best_streak = 0
epsilon = 0.010
alpha = 0.1
gamma = 0.9

obs = env.reset()
curr_state = state(obs)
print(curr_state)

for episode in range(10000):
	obs = env.reset()
	curr_state = state(obs)


	for n_iter in range(1000):
		env.render()
		action = choose_action(curr_state,epsilon)
		print "action is ",action
		state1 = state(obs)

		obs, reward, done, _ = env.step(action)
		maxQ = np.amax(q_table[curr_state])

		q_table[curr_state,action] += alpha*(reward + gamma*maxQ - q_table[curr_state,action])

		curr_state = state1

		if done:
			print("Episode %d finished after %f time steps" % (episode, n_iter))
			if(n_iter >= 199):
				num_streaks += 1
				if(num_streaks>=best_streak):
					best_streak = num_streaks
			else:
				num_streaks = 0
		break

	if num_streaks > 110:
		print("Hurrah we made it !")
		break	

env.monitor.close()





