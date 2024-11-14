import numpy as np
import gymnasium as gym 
from gymnasium import spaces 
import torch 


''' 
Notes: 
This environment is a two armed bandit that switches the probabilities of the two machines every 10 iterations.

'''

# make an 2 armed bandit environment

class BanditEnv2(gym.Env):
    
    def __init__(self):
        # 2 actions, want either first or second machine
        self.action_space = gym.spaces.Discrete(2) 
        
        # observation space is a single float, the output from the chosen machine 
        self.observation_space = gym.spaces.Box(0, 1, shape=(5,))
        
        # the two machines have different probabilities of giving a reward
        self.a = .8
        self.b = .2
        self.machine_probs = [self.a, self.b]
        self.context = 0
        self.iteration = 1
        
    
    def step(self, action): # action = 0 or 1, where 0 is the first machine and 1 is the second machine
        
        # change probability of the machines, every 10 iterations
        if self.iteration % 50 == 0:
            temp = self.a
            self.a = self.b
            self.b = temp
            self.machine_probs = [self.a, self.b]
            self.context = 1 - self.context
        
        # get reward from chosen machine
        reward = 1 if np.random.rand() < self.machine_probs[action] else 0
        
        observation = np.array([0, 0, 0, 0, 0], dtype=np.float32)
        # observation is the reward. This part seems redundant in this example?
        if action == 0:
            observation[0] = 1
        elif action == 1:
            observation[1] = 1
        observation[2] = reward
        observation[3] = self.iteration
        observation[4] = self.context
            
        
        # terminated if the episode has ended 
        terminated = True if self.iteration == 100 else False
        
        self.iteration = self.iteration + 1
        
        # info is an empty dictionary, DO NOT WRITE AS SELF.INFO = {} because it will overwrite the class variable
        info = {}
        
        # not using truncated
        truncated = False
        
        # return observation, reward, done
        return  observation, reward, terminated, truncated, info # must be in thsi order, with these names
    
  
    def reset(self, seed=None, options={}):
        # reset the iteration
        self.iteration = 1
        
        #reset the observation
        observation = np.array([0, 0, 0, 0, 0], dtype=np.float32)
        
        return observation, {} # must be in this order, with these names
    