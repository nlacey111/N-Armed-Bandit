import numpy as np
import gymnasium as gym 
from gymnasium import spaces 
import torch 


''' Questions: 

separate: how would you embed ode/pdes into any rl problem. (discretize the ode, so it can be used as a state. but how to change networks itself to include ode/pde)

followed this: https://gymnasium.farama.org/tutorials/gymnasium_basics/environment_creation/
'''

# make an 2 armed bandit environment

class BanditEnv(gym.Env):
    
    def __init__(self):
        # 2 actions, want either first or second machine
        self.action_space = gym.spaces.Discrete(2) 
        
        # observation space is a single float, the output from the chosen machine 
        self.observation_space = gym.spaces.Box(0, 1, shape=(1,))
        
        # the two machines have different probabilities of giving a reward
        self.machine_probs = [0.2, 0.7]
        
        self.iteration = 1
        
        # info is an empty dictionary
        self.info = {}
        
    
    def step(self, action): # action = 0 or 1, where 0 is the first machine and 1 is the second machine
        # get reward from chosen machine
        reward = 1 if np.random.rand() < self.machine_probs[action] else 0
        
        # observation is the reward. This part seems redundant in this example?
        observation = np.array([reward])
        
        # terminated if the episode has ended 
        terminated = True if self.iteration == 100 else False
        
        self.iteration = self.iteration + 1
        
        # info is an empty dictionary
        info = self.info
        
        # not using truncated
        truncated = False
        
        # return observation, reward, done
        return  observation, reward, terminated, truncated, info # must be in thsi order, with these names
    
  
    def reset(self):
        # reset the iteration
        self.iteration = 1
        
        #reset the observation
        observation = np.array([0])
        
        return observation, self.info # must be in this order, with these names
    