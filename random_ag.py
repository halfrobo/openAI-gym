import gym
import numpy as np



def random_learner(env,weight):
		obs = env.reset()
		totalreward = 0

		for _ in range(2000):
			env.render()
			action = 0 if np.matmul(obs,weight) < 0 else 1
			obs, reward, done, _ = env.step(action)

			totalreward +=reward
			if done:
				break
		return totalreward


best_weight = np.random.rand(4)*2 - 1

best_reward = 0

env = gym.make('CartPole-v0')

# weight = [0.04251351,-0.65644348, 0.7450335, 0.67226354]  stole a best weight combinagtion

for episode in range(1000):

	#weight = np.random.rand(4)*2 - 1

	total_rew = random_learner(env,weight)

	if total_rew > best_reward:
		best_reward = total_rew
		best_weight = weight

		if total_rew >= 200:
			print weight
			
	print "Episode number: {}".format(episode+1)
	print "Total Rewards: {}".format(total_rew)
