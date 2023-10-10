## How to Use the Package?
### Quick Start.

```python
{{ commands.import }}

log_discord = LogDiscord(webhook='https://your_discord_channel_webhook')

log_discord.send(log_level=1)   # 0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical
```