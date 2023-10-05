from logging_discord.dynaconf_config import settings
from logging_discord.send_discord import LogDiscord


class TestInit:

    #  Initializes LogDiscord with default settings
    def test_initializes_with_default_settings(self):
        # Arrange
        webhook = settings.WEBHOOK + settings.TOKEN
        avatar_url = settings.AVATAR_URL
        mode = settings.MODE
        app_name = settings.APP_NAME

        # Act
        log_discord = LogDiscord()

        # Assert
        assert log_discord.webhook == webhook
        assert log_discord.avatar_url == avatar_url
        assert log_discord.mode == mode
        assert log_discord.app_name == app_name

    #  Initializes LogDiscord with custom settings
    def test_initializes_with_custom_settings(self):
        # Arrange
        webhook = 'custom_webhook'
        avatar_url = 'custom_avatar_url'
        mode = 'custom_mode'
        app_name = 'custom_app_name'

        # Act
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)

        # Assert
        assert log_discord.webhook == webhook
        assert log_discord.avatar_url == avatar_url
        assert log_discord.mode == mode
        assert log_discord.app_name == app_name

    #  Initializes LogDiscord with custom settings and channel
    def test_initializes_with_custom_settings_and_channel(self):
        # Arrange
        webhook = 'custom_webhook'
        avatar_url = 'custom_avatar_url'
        mode = 'custom_mode'
        app_name = 'custom_app_name'
        channel = {
            'webhook': 'custom_webhook',
            'avatar_url': 'custom_avatar_url',
            'mode': 'custom_mode',
            'app_name': 'custom_app_name',
        }

        # Act
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)
        log_discord.channel = channel

        # Assert
        assert log_discord.webhook == channel['webhook']
        assert log_discord.avatar_url == channel['avatar_url']
        assert log_discord.mode == channel['mode']
        assert log_discord.app_name == channel['app_name']

    #  Initializes LogDiscord with empty webhook
    def test_initializes_with_empty_webhook(self):
        # Arrange
        webhook = ''
        avatar_url = settings.AVATAR_URL
        mode = settings.MODE
        app_name = settings.APP_NAME

        # Act
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)

        # Assert
        assert log_discord.webhook == webhook
        assert log_discord.avatar_url == avatar_url
        assert log_discord.mode == mode
        assert log_discord.app_name == app_name

    #  Initializes LogDiscord with empty avatar_url
    def test_initializes_with_empty_avatar_url(self):
        # Arrange
        webhook = settings.WEBHOOK
        avatar_url = ''
        mode = settings.MODE
        app_name = settings.APP_NAME

        # Act
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)

        # Assert
        assert log_discord.webhook == webhook
        assert log_discord.avatar_url == avatar_url
        assert log_discord.mode == mode
        assert log_discord.app_name == app_name

    #  Initializes LogDiscord with empty mode
    def test_initializes_with_empty_mode(self):
        # Arrange
        webhook = settings.WEBHOOK
        avatar_url = settings.AVATAR_URL
        mode = ''
        app_name = settings.APP_NAME

        # Act
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)

        # Assert
        assert log_discord.webhook == webhook
        assert log_discord.avatar_url == avatar_url
        assert log_discord.mode == mode
        assert log_discord.app_name == app_name
