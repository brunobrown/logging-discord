import pytest

from logging_discord.send_discord import LogDiscord


class TestSend:
    def test_if_the_data_type_is_valid(self, mocker):
        # Arrange
        log_level = 3
        log_discord = LogDiscord()
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_payload')
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_embed_list')
        mocker.patch.object(LogDiscord, '_LogDiscord__publish_record')

        # Act
        result = log_discord.send(
            show_traceback=True,
            error_message='testando mensagem de erro',
            log_level=log_level,
        )

        # Assert
        assert result

    #  Send message with default parameters
    def test_send_default_parameters(self, mocker):
        # Arrange
        webhook = 'test_webhook'
        avatar_url = 'test_avatar_url'
        mode = 'test_mode'
        app_name = 'test_app_name'
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_payload')
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_embed_list')
        mocker.patch.object(LogDiscord, '_LogDiscord__publish_record')

        # Act
        result = log_discord.send()

        # Assert
        assert result == log_discord._LogDiscord__publish_record.return_value
        log_discord._LogDiscord__generate_payload.assert_called_once_with(
            log_discord.log_levels[1]['color'],
            log_discord.log_levels[1]['emoji'],
            '',
            log_discord.log_levels[1]['title'],
        )
        log_discord._LogDiscord__generate_embed_list.assert_called_once_with(
            log_discord.log_levels[1]['color'],
            log_discord.log_levels[1]['emoji'],
            '',
            log_discord.log_levels[1]['title'],
        )
        log_discord._LogDiscord__publish_record.assert_called_once_with(
            {'wait': 'true'},
            log_discord._LogDiscord__generate_payload.return_value,
        )

    #  Send message with custom error message
    def test_send_custom_error_message(self, mocker):
        # Arrange
        webhook = 'test_webhook'
        avatar_url = 'test_avatar_url'
        mode = 'test_mode'
        app_name = 'test_app_name'
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_payload')
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_embed_list')
        mocker.patch.object(LogDiscord, '_LogDiscord__publish_record')
        error_message = 'test_error_message'

        # Act
        result = log_discord.send(error_message=error_message)

        # Assert
        assert result == log_discord._LogDiscord__publish_record.return_value
        log_discord._LogDiscord__generate_payload.assert_called_once_with(
            log_discord.log_levels[1]['color'],
            log_discord.log_levels[1]['emoji'],
            f'\n\n>>> ```error_message:\n\n{error_message}```',
            log_discord.log_levels[1]['title'],
        )
        log_discord._LogDiscord__generate_embed_list.assert_called_once_with(
            log_discord.log_levels[1]['color'],
            log_discord.log_levels[1]['emoji'],
            f'\n\n>>> ```error_message:\n\n{error_message}```',
            log_discord.log_levels[1]['title'],
        )
        log_discord._LogDiscord__publish_record.assert_called_once_with(
            {'wait': 'true'},
            log_discord._LogDiscord__generate_payload.return_value,
        )

    #  Send message with custom log level
    def test_send_custom_log_level(self, mocker):
        # Arrange
        webhook = 'test_webhook'
        avatar_url = 'test_avatar_url'
        mode = 'test_mode'
        app_name = 'test_app_name'
        log_discord = LogDiscord(webhook, avatar_url, mode, app_name)
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_payload')
        mocker.patch.object(LogDiscord, '_LogDiscord__generate_embed_list')
        mocker.patch.object(LogDiscord, '_LogDiscord__publish_record')
        log_level = 3

        # Act
        result = log_discord.send(log_level=log_level)

        # Assert
        assert result == log_discord._LogDiscord__publish_record.return_value
        log_discord._LogDiscord__generate_payload.assert_called_once_with(
            log_discord.log_levels[log_level]['color'],
            log_discord.log_levels[log_level]['emoji'],
            '',
            log_discord.log_levels[log_level]['title'],
        )
        log_discord._LogDiscord__generate_embed_list.assert_called_once_with(
            log_discord.log_levels[log_level]['color'],
            log_discord.log_levels[log_level]['emoji'],
            '',
            log_discord.log_levels[log_level]['title'],
        )
        log_discord._LogDiscord__publish_record.assert_called_once_with(
            {'wait': 'true'},
            log_discord._LogDiscord__generate_payload.return_value,
        )
