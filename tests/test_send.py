from logging_discord.send_discord import LogDiscord

log_discord = LogDiscord()


def test_data_type():
    # Arrange
    log_level = 'number'

    # Act
    result = log_discord.send(
        show_traceback=True,
        error_message='testando mensagem de erro',
        log_level=log_level,
    )

    # Assert
    assert result
