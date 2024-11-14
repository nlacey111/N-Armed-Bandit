import numpy as np
import gymnasium as gym 
from gymnasium import spaces 
import torch 


''' 
Notes: 
This is a 2 armed bandit where the probabilities of the two machines changes according to a continuous function. 

'''

# make an 2 armed bandit environment

class BanditEnv1(gym.Env):
    
    def __init__(self):
        # 2 actions, want either first or second machine
        self.action_space = gym.spaces.Discrete(2) 
        
        # observation space is a single float, the output from the chosen machine 
        self.observation_space = gym.spaces.Box(0, 1, shape=(1,))
        
        # the two machines have different probabilities of giving a reward
        a = .8
        b = .2
        self.machine_probs = [a, b]
        
        self.iteration = 1
        
    
    def step(self, action): # action = 0 or 1, where 0 is the first machine and 1 is the second machine
        
        # change probability of the machines, according to a continuous function
        P = 10000
        Q = 100
        fixed_prob = 0.5
        
        a = fixed_prob*1/(1 + np.exp(-Q*np.sin( 2*np.pi*self.iteration/P)))

        b = fixed_prob*1/(1 + np.exp(-Q*np.cos( 2*np.pi*self.iteration/P + 2*np.pi/128)))
        self.machine_probs = [a, b]
        
        # get reward from chosen machine
        reward = 1 if np.random.rand() < self.machine_probs[action] else 0
        
        # observation is the reward. This part seems redundant in this example?
        observation = np.array([reward])
        
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
        observation = np.array([0])
        
        return observation, {} # must be in this order, with these names
    
    
    