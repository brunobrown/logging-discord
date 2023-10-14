from logging_discord import LogDiscord


class TestRemoveExtraCharacters:

    #  Test with error_traceback length less than self.__number_characters
    def test_error_traceback_length_less_than_number_characters(self):
        # Arrange
        log_discord = LogDiscord()
        error_traceback = 'This is a short error traceback.'

        # Act
        result = log_discord._LogDiscord__remove_extra_characters(
            error_traceback
        )

        # Assert
        assert result == error_traceback

    #  Test with error_traceback length equal to self.__number_characters
    def test_error_traceback_length_equal_to_number_characters(self):
        # Arrange
        log_discord = LogDiscord()
        error_traceback = 'a' * log_discord._LogDiscord__number_characters

        # Act
        result = log_discord._LogDiscord__remove_extra_characters(
            error_traceback
        )

        # Assert
        assert result == error_traceback

    # Test with error_traceback length greater than self.__number_characters
    # but less than self.__number_characters + 4
    def test_error_traceback_length_greater_than_number_characters_but_less_than_number_characters_plus_4(
        self,
    ):
        # Arrange
        log_discord = LogDiscord()
        error_traceback = 'a' * log_discord._LogDiscord__number_characters

        # Act
        result = log_discord._LogDiscord__remove_extra_characters(
            error_traceback
        )

        # Assert
        assert result == error_traceback

    #  Test with error_traceback length equal to self.__number_characters + 4
    def test_error_traceback_length_equal_to_number_characters_plus_4(self):
        # Arrange
        log_discord = LogDiscord()
        error_traceback = 'a' * log_discord._LogDiscord__number_characters

        # Act
        result = log_discord._LogDiscord__remove_extra_characters(
            error_traceback
        )

        # Assert
        assert result == error_traceback

    #  Test with error_traceback length greater
    #  than self.__number_characters + 4
    def test_error_traceback_length_greater_than_number_characters_plus_4(
        self,
    ):
        # Arrange
        log_discord = LogDiscord()
        error_traceback = 'a' * log_discord._LogDiscord__number_characters

        # Act
        result = log_discord._LogDiscord__remove_extra_characters(
            error_traceback
        )

        # Assert
        assert (
            result
            == f'{error_traceback[-(log_discord._LogDiscord__number_characters):]}'
        )

    #  Test with empty error_traceback
    def test_empty_error_traceback(self):
        # Arrange
        log_discord = LogDiscord()
        error_traceback = ''

        # Act
        result = log_discord._LogDiscord__remove_extra_characters(
            error_traceback
        )

        # Assert
        assert result == error_traceback

    def test_remove_extra_characters_no_change(self):
        # Arrange: Cria um traceback sem caracteres extras
        log_discord = LogDiscord()
        traceback = 'This is a normal traceback.'

        # Act: Chama o método __remove_extra_characters
        cleaned_traceback = log_discord._LogDiscord__remove_extra_characters(
            traceback
        )

        # Assert: Verifica se o resultado é o mesmo que o traceback original
        assert cleaned_traceback == traceback

    def test_remove_extra_characters_with_extra_characters(self):
        # Arrange: Cria um traceback com caracteres extras
        log_discord = LogDiscord()
        traceback = 'X' * 8000 + 'This is the actual traceback.'

        # Act: Chama o método __remove_extra_characters
        cleaned_traceback = log_discord._LogDiscord__remove_extra_characters(
            traceback
        )

        # Assert: Verifica se os caracteres extras foram removidos
        assert '...' in cleaned_traceback
        assert len(cleaned_traceback) == 6018  # Tamanho máximo permitido

    def test_remove_extra_characters_length_limit(self):
        # Arrange: Cria um traceback com um tamanho maior do que o limite
        log_discord = LogDiscord()
        traceback = 'X' * 6018

        # Act: Chama o método __remove_extra_characters
        cleaned_traceback = log_discord._LogDiscord__remove_extra_characters(
            traceback
        )

        # Assert: Verifica se o tamanho foi reduzido para o limite máximo
        assert len(cleaned_traceback) == 6018
