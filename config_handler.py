from environs import Env


def get_config(config_name: str):
    from config import config_selector

    env = Env()
    app_env = env.str('APP_ENV')

    config = config_selector[app_env]
    requested_config_value = getattr(config, config_name)
    return requested_config_value
