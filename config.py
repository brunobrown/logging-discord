from dynaconf import Dynaconf


# current_directory = os.path.dirname(os.path.realpath(__file__))

settings = Dynaconf(
    environments=True,
    load_dotenv=False,
    # settings_files=[
    #     f"{current_directory}/settings.toml",
    #     f"{current_directory}/.secrets.toml"
    # ],
    settings_files=['settings.toml', '.secrets.toml'],
    envvar_prefix='LOG_DISCORD',
    enviroments=['development', 'production'],
    env_switcher='LOG_DISCORD_MODE',
)
