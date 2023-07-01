from __future__ import annotations

import logging
import traceback

import httpx

from config import settings

LOG_LEVELS = {
    'unknown': 0,
    'debug': 1,
    'info': 2,
    'warning': 3,
    'error': 4,
    'critical': 5,
}

DATA_LOG = [
    #   color legend:
    #   * 2040357 = Black
    #   * 8947848 = Gray
    #   * 2196944 = Blue
    #   * 16497928 = Yellow
    #   * 14362664 = Red
    {'emoji': ':thinking:   ', 'title': 'UNKNOWN ERROR', 'color': 2040357},
    {'emoji': ':bug:   ', 'title': 'DEBUG', 'color': 8947848},
    {'emoji': ':information_source:   ', 'title': 'INFO', 'color': 2196944},
    {'emoji': ':warning:   ', 'title': 'WARNING', 'color': 16497928},
    {'emoji': ':x:   ', 'title': 'ERROR', 'color': 14362664},
    {'emoji': ':sos:   ', 'title': 'CRITICAL', 'color': 14362664},
]


class LogDiscord:
    """
    Registra mensagens de erros no Discord.

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

    def __init__(
        self,
        webhook: str = settings.discord.WEBHOOK,
        avatar_url: str = settings.development.AVATAR_URL,
        mode: str = 'DEVELOPMENT',
        app_name: str = 'APP_TEST',
    ):

        self.webhook = webhook
        self.avatar_url = avatar_url
        self.mode = mode
        self.app_name = app_name
        self.number_characters = 6000

    def send(
        self,
        show_traceback: bool = True,
        error_message: str = '',
        log_level: int = 1,
    ):
        """
        Envia mensagens de erro no Discord.

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

        if show_traceback and traceback.format_exc() != 'NoneType: None\n':
            error_traceback = traceback.format_exc()

        if error_message:
            error_message = f' \n > **error_message**: {error_message}'

        error_traceback = f'{error_traceback}{error_message}'

        if not isinstance(log_level, int):
            log_level = 1

        emoji = DATA_LOG[log_level]['emoji']
        title = DATA_LOG[log_level]['title']
        color = DATA_LOG[log_level]['color']

        params = {
            'wait': 'true',
        }

        payload = self.__generate_payload(color, emoji, error_traceback, title)

        if len(error_traceback) > self.number_characters - 1904:

            if len(error_traceback) > self.number_characters:
                error_traceback = (
                    '... '
                    + error_traceback[
                        len(error_traceback)
                        - self.number_characters
                        - 4 : len(error_traceback)
                    ]
                )

            text_size = 4096
            embeds = []

            for index in range(0, len(error_traceback), text_size):

                if index == 0:
                    embeds.append(
                        {
                            'title': f'{emoji}{self.mode.upper()} - {title}',
                            'description': f'_ _ \n {error_traceback[index:index + text_size - 83]} ...',
                            'color': color,
                        }
                    )
                    continue

                embeds.append(
                    {
                        'title': 'continuation',
                        'description': f'_ _ \n ... {error_traceback[index:index + text_size]}',
                        'color': color,
                    }
                )

            payload['embeds'] = embeds

        try:
            response = httpx.post(self.webhook, params=params, json=payload)
            print(f'DISCORD_RESPONSE: {response.text}')
            return response.text

        except Exception as error:
            logging.exception(
                f'falha ao tentar enviar log para o discord. Error: {error}'
            )

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
    log_discord = LogDiscord()
    try:
        25/0
    except Exception as error:
        result = log_discord.send(log_level=3)

    print(result)
