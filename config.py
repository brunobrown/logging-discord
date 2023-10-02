from dynaconf import Dynaconf

settings = Dynaconf(
    # environments=True,
    envvar_prefix='log_discord_',
    settings_files=['settings.toml', '.secrets.toml'],
    enviroments=['development', 'production'],
    env_switcher='MODE',
)
