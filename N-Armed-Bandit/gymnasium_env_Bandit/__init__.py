from gymnasium.envs.registration import register

register(
    id="gymnasium_env_Bandit/Bandit-v0",
    entry_point="gymnasium_env_Bandit.envs:BanditEnv",
)
