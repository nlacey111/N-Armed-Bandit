from gymnasium.envs.registration import register

register(
    id="gymnasium_env_Bandit/Bandit-v0",
    entry_point="gymnasium_env_Bandit.envs:BanditEnv",
)

register(
    id = "gymnasium_env_Bandit/Bandit-cont-switch",
    entry_point="gymnasium_env_Bandit.envs:BanditEnv1",
)

register( 
         id = "gymnasium_env_Bandit/Bandit-flipflop",
    entry_point="gymnasium_env_Bandit.envs:BanditEnv2",
)
