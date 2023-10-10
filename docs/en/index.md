![Project Logo](
    assets/img/logo.png
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

If you prefer to make a donation via PIX, please follow the instructions below:

1. Open your banking app.
2. Select the transfer or payment option.
3. Choose the PIX option.
4. Enter the following details:
   - PIX Key: [Insert your PIX key here]
   - Amount: [Insert the donation amount]
5. Confirm the transaction.

**PIX QR Code:**
![PIX QR Code](link_to_your_pix_qr_code.png)

### Bitcoin

I accept donations in Bitcoin. If you wish to make a Bitcoin donation, please use the
following wallet:

- Bitcoin Wallet: [Insert your Bitcoin wallet address here]

**Bitcoin QR Code:**
![Bitcoin QR Code](link_to_your_bitcoin_qr_code.png)

Your contribution helps me to keep improving the project and providing support to the user community. I appreciate your support!

!!! info "About"
    Add something here