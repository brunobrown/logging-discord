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

## How to Contribute to the Project?
Thank you for your interest in contributing to the **Logging Discord** project! :heart:

## Tests
We use [pytest](https://pytest.org/) for testing. Configuration details can be found in the
[pyproject.toml](https://github.com/brunobrown/logging-discord/blob/master/pyproject.toml) file at the project's root.

For tasks not listed here, you can refer to the [issues](https://github.com/brunobrown/logging-discord/issues).

## Support the Project

Thank you for considering supporting the project! Your help is greatly appreciated and it enables me
to continue developing and maintaining the software.

There are two ways to make donations:

### PIX

If you prefer to make a donation via PIX:

   - [PIX or QR Code](https://nubank.com.br/pagar/az4ws/snv4Ud3fJk)

![Nubank QR Code:](img/nubank_qrcode.png)

### Bitcoin

I accept donations in Bitcoin. If you wish to make a Bitcoin donation, please use the
following wallet:

- Bitcoin Wallet: 3QvDoHGUhYksbb9NkoEj7H45md48GXsnp6

![Bitcoin QR Code](img/bitcoin_qrcode.png)

Your contribution helps me to keep improving the project and providing support to the user community. I appreciate your support!

!!! info "About"
    Add something here