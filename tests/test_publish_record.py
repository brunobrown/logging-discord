from unittest.mock import patch

import pytest

from logging_discord.send_discord import LogDiscord


@pytest.fixture
def log_discord():
    # Configuração inicial com um webhook de teste
    return LogDiscord(webhook='https://example.com/test_webhook')


@patch('httpx.post')  # Mock para httpx.post para evitar chamadas reais de rede
def test_publish_record_success(mock_httpx_post, log_discord):
    # Arrange: Configurar o mock para retornar uma resposta de sucesso
    mock_httpx_post.return_value.text = 'Mensagem enviada com sucesso'

    # Act: Chamar o método __publish_record
    response = log_discord._LogDiscord__publish_record({}, {})

    # Assert: Verificar se a resposta é a esperada
    assert response == 'Mensagem enviada com sucesso'


@patch('httpx.post')  # Mock para httpx.post para evitar chamadas reais de rede
def test_publish_record_failure(mock_httpx_post, log_discord):
    # Arrange: Simular uma exceção ao enviar a mensagem
    mock_httpx_post.side_effect = Exception('Erro ao enviar a mensagem')

    # Act: Chamar o método __publish_record
    response = log_discord._LogDiscord__publish_record({}, {})

    # Assert: Verificar se a resposta indica uma falha esperada
    assert 'Erro ao enviar a mensagem' in response
