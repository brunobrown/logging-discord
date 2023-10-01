from logging_discord.send_discord import LogDiscord


class TestPublishRecord:
    #  Sends a valid payload to Discord API and returns the response text.
    def test_sends_valid_payload_and_returns_response_text(self, mocker):
        # Arrange
        params = {'wait': 'true'}
        payload = {
            'content': '_ _',
            'embeds': [
                {
                    'title': ':information_source:   DEVELOPMENT - INFO',
                    'description': '_ _ \n error_traceback',
                    'color': 2196944,
                }
            ],
            'username': 'app_name',
            'avatar_url': 'avatar_url',
            'attachments': [],
        }
        response_text = 'Response from Discord API'
        mocker.patch(
            'httpx.post',
            return_value=mocker.Mock(text=response_text),
        )
        log_discord = LogDiscord()

        # Act
        result = log_discord._LogDiscord__publish_record(params, payload)

        # Assert
        assert result == response_text

    # Sends a payload with empty embeds to Discord API and returns the
    # response text.
    def test_sends_payload_with_empty_embeds_and_returns_response_text(
        self, mocker
    ):
        # Arrange
        params = {'wait': 'true'}
        payload = {
            'content': '_ _',
            'embeds': [],
            'username': 'app_name',
            'avatar_url': 'avatar_url',
            'attachments': [],
        }
        response_text = 'Response from Discord API'
        mocker.patch(
            'httpx.post',
            return_value=mocker.Mock(text=response_text),
        )
        log_discord = LogDiscord()

        # Act
        result = log_discord._LogDiscord__publish_record(params, payload)

        # Assert
        assert result == response_text

    # Sends a payload with empty content to Discord API and returns the
    # response text.
    def test_sends_payload_with_empty_content_and_returns_response_text(
        self, mocker
    ):
        # Arrange
        params = {'wait': 'true'}
        payload = {
            'content': '',
            'embeds': [
                {
                    'title': ':information_source:   DEVELOPMENT - INFO',
                    'description': '_ _ \n error_traceback',
                    'color': 2196944,
                }
            ],
            'username': 'app_name',
            'avatar_url': 'avatar_url',
            'attachments': [],
        }
        response_text = 'Response from Discord API'
        mocker.patch(
            'httpx.post',
            return_value=mocker.Mock(text=response_text),
        )
        log_discord = LogDiscord()

        # Act
        result = log_discord._LogDiscord__publish_record(params, payload)

        # Assert
        assert result == response_text

    # Sends a payload with empty username to Discord API and returns the
    # response text.
    def test_sends_payload_with_empty_username_and_returns_response_text(
        self, mocker
    ):
        # Arrange
        params = {'wait': 'true'}
        payload = {
            'content': '_ _',
            'embeds': [
                {
                    'title': ':information_source:   DEVELOPMENT - INFO',
                    'description': '_ _ \n error_traceback',
                    'color': 2196944,
                }
            ],
            'username': '',
            'avatar_url': 'avatar_url',
            'attachments': [],
        }
        response_text = 'Response from Discord API'
        mocker.patch(
            'httpx.post',
            return_value=mocker.Mock(text=response_text),
        )
        log_discord = LogDiscord()

        # Act
        result = log_discord._LogDiscord__publish_record(params, payload)

        # Assert
        assert result == response_text

    # Sends a payload with empty avatar_url to Discord API and returns the
    # response text.
    def test_sends_payload_with_empty_avatar_url_and_returns_response_text(
        self, mocker
    ):
        # Arrange
        params = {'wait': 'true'}
        payload = {
            'content': '_ _',
            'embeds': [
                {
                    'title': ':information_source:   DEVELOPMENT - INFO',
                    'description': '_ _ \n error_traceback',
                    'color': 2196944,
                }
            ],
            'username': 'app_name',
            'avatar_url': '',
            'attachments': [],
        }
        response_text = 'Response from Discord API'
        mocker.patch(
            'httpx.post',
            return_value=mocker.Mock(text=response_text),
        )
        log_discord = LogDiscord()

        # Act
        result = log_discord._LogDiscord__publish_record(params, payload)

        # Assert
        assert result == response_text

    def test_publish_record_success(self, mocker):
        # Arrange: Configurar o mock para retornar uma resposta de sucesso
        params = {'wait': 'true'}
        payload = {
            'content': '_ _',
            'embeds': [
                {
                    'title': ':information_source:   DEVELOPMENT - INFO',
                    'description': '_ _ \n error_traceback',
                    'color': 2196944,
                }
            ],
            'username': 'app_name',
            'avatar_url': '',
            'attachments': [],
        }
        response_text = 'Mensagem enviada com sucesso'
        mocker.patch(
            'httpx.post',
            return_value=mocker.Mock(text=response_text),
        )
        log_discord = LogDiscord()

        # Act: Chamar o método __publish_record
        response = log_discord._LogDiscord__publish_record(params, payload)

        # Assert: Verificar se a resposta é a esperada
        assert response == 'Mensagem enviada com sucesso'

    def test_publish_record_failure(self, mocker):
        # Arrange: Simular uma exceção ao enviar a mensagem
        params = {'wait': 'true'}
        payload = {
            'content': '_ _',
            'embeds': [
                {
                    'title': ':information_source:   DEVELOPMENT - INFO',
                    'description': '_ _ \n error_traceback',
                    'color': 2196944,
                }
            ],
            'username': 'app_name',
            'avatar_url': '',
            'attachments': [],
        }
        response_text = 'Mensagem enviada com sucesso'
        # Mock para httpx.post para evitar chamadas reais de rede
        mocker.patch(
            'httpx.post',
            return_value=mocker.Mock(text=response_text),
            side_effect=Exception('Erro ao enviar a mensagem'),
        )
        log_discord = LogDiscord()

        # Act: Chamar o método __publish_record
        response = log_discord._LogDiscord__publish_record(params, payload)

        # Assert: Verificar se a resposta indica uma falha esperada
        assert 'Erro ao enviar a mensagem' in response
