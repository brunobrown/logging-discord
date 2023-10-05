from __future__ import annotations

from dynaconf import Dynaconf


# current_directory = Path(__file__).parents[1]

settings = Dynaconf(
    environments=True,
    load_dotenv=False,
    settings_files=['settings.toml', '.secrets.toml'],
    envvar_prefix='LOG_DISCORD',
    enviroments=['development', 'production'],
    env_switcher='LOG_DISCORD_MODE',
)
