from __future__ import annotations

import logging
import traceback

import httpx

from logging_discord.dynaconf_config import settings


class LogDiscord:
    """
    A classe LogDiscord é responsável por registrar mensagens de erro no
    Discord. Recebe como parâmetros um webhook, a URL do avatar, um modo e
    um nome de aplicativo. Possui um método send
    que envia mensagens de erro para o Discord, com a opção de mostrar um
    traceback e uma mensagem de erro.

    Caso deseje, também é possível criar um arquivo de configurações contendo
    as informações de acesso para o seu canal no Discord e a customização dos
    seus logs. Para mais informações, visite:
    https://logging-discord.readthedocs.io/en/latest/#configuration-via-discord_configpy

    Parameters

        webhook: str
            Webhook do canal no discord.
        avatar_url: str
            URL do avatar.
        mode: str
            Modo de desenvolvimento.
            Exemplo:
                DEVELOPMENT
                HOMOLOGATION
                PRODUCTION
        app_name: str
            Nome do aplicativo.

    """

    try:
        webhook = settings.WEBHOOK + settings.TOKEN
        avatar_url = settings.AVATAR_URL
        mode = settings.MODE
        app_name = settings.APP_NAME

    except AttributeError:
        webhook = 'https://discord.com/api/webhooks/your_token_here'
        avatar_url = (
            'https://i0.wp.com/www.theterminatorfans.com/wp-content'
            '/uploads/2012/09/the-terminator3.jpg?resize=900%2C450&ssl=1'
        )
        mode = 'DEVELOPMENT'
        app_name = 'APP_TEST'

    try:
        from discord_config import channel
        from discord_config import log_levels

    except ImportError:
        from logging_discord.default import log_levels

    def __init__(
        self,
        webhook: str = webhook,
        avatar_url: str = avatar_url,
        mode: str = mode,
        app_name: str = app_name,
    ):

        # test = settings.current_env
        # print(test)

        self.webhook = webhook
        self.avatar_url = avatar_url
        self.mode = mode
        self.app_name = app_name
        self.__number_characters = 6010

        if hasattr(self, 'channel'):
            self.webhook = self.channel.get('webhook')
            self.avatar_url = self.channel.get('avatar_url')
            self.mode = self.channel.get('mode')
            self.app_name = self.channel.get('app_name')

    def send(
        self,
        show_traceback: bool = True,
        error_message: str = '',
        log_level: int = 1,
    ) -> str:
        """
        Envia mensagens de erro para o Discord, com a opção de mostrar um
        traceback e uma mensagem erro.

        Parameters

        show_traceback: bool
            Exibe o traceback.
        error_message: str
            Mensagem de erro que será exibida junto ao traceback.
        log_level: int
            Define qual será o nível de log |
            Exemplo:
                0 = unknown
                1 = debug
                2 = info
                3 = warning
                4 = error
                5 = critical

        Exemple:
            log_discord.send(
                show_traceback=True,
                error_message='testando mensagem de erro',
                log_level=3
            )

        """

        error_traceback = ''
        params = {
            'wait': 'true',
        }

        if show_traceback and traceback.format_exc() != 'NoneType: None\n':
            error_traceback = traceback.format_exc()

        if error_message:
            error_message = f'\n\n>>> ```error_message:\n\n{error_message}```'

        error_traceback = f'{error_traceback}{error_message}'

        if not isinstance(log_level, int):
            log_level = 1

        emoji = self.log_levels[log_level]['emoji']
        title = self.log_levels[log_level]['title']
        color = self.log_levels[log_level]['color']

        payload = self.__generate_payload(color, emoji, error_traceback, title)

        embeds = self.__generate_embed_list(
            color, emoji, error_traceback, title
        )

        if embeds:
            payload['embeds'] = embeds

        return self.__publish_record(params, payload)

    def __publish_record(self, params, payload) -> str:
        """
        Publica o registro no Discord.
        """

        try:
            response = httpx.post(self.webhook, params=params, json=payload)
            print(f'DISCORD_RESPONSE: {response.text}')
            return response.text

        except (
            httpx.RequestError,
            httpx.HTTPError,
            Exception,
        ) as publish_record_error:

            logging.exception(
                f'falha ao tentar enviar log para o discord. '
                f'Error: {publish_record_error}'
            )

            return (
                f'falha ao tentar enviar log para o discord. '
                f'Error: {publish_record_error}'
            )

    def __generate_embed_list(self, color, emoji, error_traceback, title):
        """
        Gera a lista de incorporação.

        Parameters

        color: str
            Cor do texto

        emoji: str
            Emoji do texto

        error_traceback: str
            Traceback do error

        title: str
            Titulo do log

        Return:
            payload: dict

        """

        MAX_ERROR_TRACEBACK_LENGTH = 1904
        TEXT_SIZE = 4096
        embeds = []

        if (
            len(error_traceback)
            > self.__number_characters - MAX_ERROR_TRACEBACK_LENGTH
        ):

            error_traceback = self.__remove_extra_characters(error_traceback)

            for index in range(0, len(error_traceback), TEXT_SIZE):

                if index == 0:
                    embeds.append(
                        {
                            'title': f'{emoji}{self.mode.upper()} - {title}',
                            'description': f'_ _ \n {error_traceback[index:index + TEXT_SIZE - 83]} ...',
                            'color': color,
                        }
                    )
                    continue

                embeds.append(
                    {
                        'title': 'continuation',
                        'description': f'_ _ \n ... {error_traceback[index:index + TEXT_SIZE]}',
                        'color': color,
                    }
                )

        return embeds

    def __remove_extra_characters(self, error_traceback):
        """
        Remove caracteres extras do error_traceback fornecido se seu
        comprimento for maior que `self.__number_characters`.

        Este método recebe uma string de rastreamento de erro como entrada.
        Se o comprimento do traceback de erro for maior que
        `self.__number_characters`, o método removerá caracteres extras do
        início da string de traceback e os substituirá por reticências (...),
        e mantendo o último `self.__number_characters` menos 4 caracteres.

        Parameters:
            error_traceback (str): The error traceback string.

        Returns:
            str: The modified error traceback string.
        """
        if len(error_traceback) > self.__number_characters:
            error_traceback = f"""... {
            error_traceback[
            len(error_traceback)
            - self.__number_characters
            - 4: len(error_traceback)
            ]
            }"""

        return error_traceback

    def __generate_payload(self, color, emoji, error_traceback, title):
        """
        Gera a estrutura de payload

        Parameters

        color: str
            Cor do texto

        emoji: str
            Emoji do texto

        error_traceback: str
            Traceback do error

        title: str
            Titulo do log

        Return:
            payload: dict

        """
        payload = {
            'content': '_ _',
            'embeds': [
                {
                    'title': f'{emoji}{self.mode.upper()} - {title}',
                    'description': f'_ _ \n {error_traceback}',
                    'color': color,
                }
            ],
            'username': self.app_name,
            'avatar_url': self.avatar_url,
            'attachments': [],
        }
        return payload


if __name__ == '__main__':

    log_discord = LogDiscord(mode='DEVELOPMENT')
    try:
        raise Exception(f'{"x" * 3000 + "B"}')

    except Exception as error:
        result = log_discord.send(
            log_level=3,
            error_message='Testando o envio ...',
        )

        print(result)
