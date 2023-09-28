import pytest

from logging_discord.send_discord import LogDiscord


@pytest.fixture
def log_discord():
    # Configuração inicial com um objeto LogDiscord de teste
    return LogDiscord()


def test_remove_extra_characters_no_change(log_discord):
    # Arrange: Cria um traceback sem caracteres extras
    traceback = 'This is a normal traceback.'

    # Act: Chama o método __remove_extra_characters
    cleaned_traceback = log_discord._LogDiscord__remove_extra_characters(
        traceback
    )

    # Assert: Verifica se o resultado é o mesmo que o traceback original
    assert cleaned_traceback == traceback


def test_remove_extra_characters_with_extra_characters(log_discord):
    # Arrange: Cria um traceback com caracteres extras
    traceback = 'X' * 8000 + 'This is the actual traceback.'

    # Act: Chama o método __remove_extra_characters
    cleaned_traceback = log_discord._LogDiscord__remove_extra_characters(
        traceback
    )

    # Assert: Verifica se os caracteres extras foram removidos
    assert '...' in cleaned_traceback
    assert len(cleaned_traceback) == 6018  # Tamanho máximo permitido


def test_remove_extra_characters_length_limit(log_discord):
    # Arrange: Cria um traceback com um tamanho maior do que o limite
    traceback = 'X' * 6018

    # Act: Chama o método __remove_extra_characters
    cleaned_traceback = log_discord._LogDiscord__remove_extra_characters(
        traceback
    )

    # Assert: Verifica se o tamanho foi reduzido para o limite máximo
    assert len(cleaned_traceback) == 6018
