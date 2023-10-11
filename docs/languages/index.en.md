![Project Logo](
    img/logo.png
){ width='250px' .center }

# Logging Discord
This project was created with the purpose of sending the entire traceback or a portion of it along with an
error message to Discord if necessary.

## How to Install the Package?
```bash
pip install logging_discord

```

## How to Use the Package?
### Quick Start.

```python
{{ commands.import }}

log_discord = LogDiscord(webhook='https://your_discord_channel_webhook')

log_discord.send(log_level=1)   # 0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical
```

## Configuration via `discord_config.py`

You can configure the parameters of the LogDiscord class by creating a file
called 'discord_config.py' at the root of your project. The 'discord_config.py'
file should contain the following configurations:

### Exemplo:

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

!!! info "Note"
    Remember to adjust the parameters according to your needs and customize error messages as necessary.

---

## How to Contribute to the Project?
Thank you for your interest in contributing to the **Logging Discord** project! :heart:

### Tests
We use [pytest](https://pytest.org/) for testing. Configuration details can be found in the
[pyproject.toml](https://github.com/brunobrown/logging-discord/blob/master/pyproject.toml) file at the project's root.

For tasks not listed here, you can refer to the [issues](https://github.com/brunobrown/logging-discord/issues){ target="_blank" }.

---

## Support the Project

Thank you for considering supporting the project! Your help is greatly appreciated and it enables me
to continue developing and maintaining the software.

There are two ways to make donations:

!!! info "PIX"

    If you prefer to make a donation via PIX:

    - [PIX or QR Code](https://nubank.com.br/pagar/az4ws/snv4Ud3fJk){ target="_blank" }

    ![Nubank QR Code:](img/nubank_qrcode.png){ .center }


!!! info "Bitcoin"

    I accept donations in Bitcoin. If you wish to make a Bitcoin donation, please use the
    following wallet:

    - Bitcoin Wallet: 3QvDoHGUhYksbb9NkoEj7H45md48GXsnp6

    ![Bitcoin QR Code](img/bitcoin_qrcode.png){ .center }


Your contribution helps me to keep improving the project and providing support to the user community. I appreciate your support!