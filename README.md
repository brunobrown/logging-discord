<img src="https://logging-discord.readthedocs.io/en/latest/img/logging_discord.png" width="350">

# Logging Discord
[![Documentation Status](https://readthedocs.org/projects/logging-discord/badge/?version=latest)](https://logging-discord.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/brunobrown/logging-discord/actions/workflows/pipeline.yml/badge.svg)](https://github.com/brunobrown/logging-discord/actions/workflows/pipeline.yml)
[![codecov](https://codecov.io/gh/brunobrown/logging-discord/graph/badge.svg?token=XTB97RAJA6)](https://codecov.io/gh/brunobrown/logging-discord)

- [English](README.md)
- [Português](README-pt.md)

The `Logging Discord` is a tool that simplifies the logging of error messages to a Discord channel. It allows you to send error messages with custom information, including a traceback and specific messages. Below, you will find details, parameters and methods, as well as usage examples.

## Table of Contents

- [How to Install the Package?](#how-to-install-the-package)
- [How to Use the Package?](#how-to-use-the-package)
- [Configuration via 'discord_config.py'](#configuration-via-discord_configpy)
- [Usage Examples](#usage-examples)
- [Donations](#donations)

## How to Install the Package?

```bash
pip install logging_discord

```

## How to Use the Package?
### Quick Start.

```python
from logging_discord import LogDiscord

log_discord = LogDiscord(webhook='https://your_discord_channel_webhook')

log_discord.send(log_level=1)   # 0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical
```

<img src="https://logging-discord.readthedocs.io/en/latest/img/error_message.png">

---

## Configuration with `discord_config.py`

You can configure the parameters of the `LogDiscord` class by creating a file called 'discord_config.py' at the root of the project. The 'discord_config.py' file should contain the following configurations:

Example:

```python
channel = {
    'webhook': 'https://discord.com/api/webhooks/example',
    'avatar_url': 'https://i0.wp.com/www.theterminatorfans.com/wp-content/uploads/2012/09/the-terminator3.jpg?resize=900%2C450&ssl=1',
    'mode': 'DEVELOPMENT',
    'app_name': 'APP_TEST',
}

log_levels = {
    #   color legend:
    #   * 2040357 = Black
    #   * 8947848 = Gray
    #   * 2196944 = Blue
    #   * 16497928 = Yellow
    #   * 14362664 = Red
    
    0: {
        'emoji': ':thinking:   ',
        'title': 'UNKNOWN ERROR',
        'color': 2040357,
    },
    1: {'emoji': ':bug:   ', 'title': 'DEBUG', 'color': 8947848},
    2: {
        'emoji': ':information_source:   ',
        'title': 'INFO',
        'color': 2196944,
    },
    3: {'emoji': ':warning:   ', 'title': 'WARNING', 'color': 16497928},
    4: {'emoji': ':x:   ', 'title': 'ERROR', 'color': 14362664},
    5: {'emoji': ':sos:   ', 'title': 'CRITICAL', 'color': 14362664},
}
```

---

## Usage Examples

Here are some examples of how to use the `LogDiscord` class:

```python
# Creating a logger instance
logger = LogDiscord(webhook="your_webhook_url", avatar_url="avatar_url", mode="DEVELOPMENT", app_name="MyApp")

# Sending an error log with traceback
logger.send(show_traceback=True, error_message="Critical error occurred!", log_level=5)

# Sending an information log
logger.send(show_traceback=False, error_message="Operation successful.", log_level=2)
```

#### Remember to adjust the parameters according to your needs and customize error messages as necessary.

---

## Donations

Thank you for considering supporting the project! Your help is greatly appreciated and it enables me to continue developing and maintaining the software.

[Support the Project](https://logging-discord.readthedocs.io/en/latest/#support-the-project)

---

<img src="https://logging-discord.readthedocs.io/en/latest/img/proverbs_16_3.jpg" width="500">

[Commit your work to the LORD, and your plans will succeed. Proverbs 16: 3](https://www.bible.com/bible/116/PRO.16.NLT)

