import logging
import traceback
import httpx
from data_log import DATA_LOG

LOG_LEVELS = {
    'unknown': 0,
    'debug': 1,
    'info': 2,
    'warning': 3,
    'error': 4,
    'critical': 5
}


class LogDiscord:
    """
    Registra mensagens de erros no Discord.

    Parameters

        webhook: str
            URL do webhook.
        avatar_url: str
            URL do avatar.
        mode: str
            Modo de desenvolvimento.
            Exemplo:
                DEVELOPMENT
                HOMOLOGATION
                PRODUCTION

        app_name: str
            Nome do app.

    """

    def __init__(
            self,
            webhook: str = 'https://discord.com/api/webhooks/1089503453132361728/MijZoB0KnGn4j3_HbtEeYbuqMutgU_pZaHcAf1M4lzbCWOJX2VLIbPDrPHXNYe78PcMu',
            avatar_url: str = 'https://i0.wp.com/www.theterminatorfans.com/wp-content/uploads/2012/09/the-terminator3.jpg?resize=900%2C450&ssl=1',
            mode: str = 'DEVELOPMENT',
            app_name: str = 'APP_TEST'
    ):

        self.webhook = webhook
        self.avatar_url = avatar_url
        self.mode = mode
        self.app_name = app_name

    def send(self, **kwargs):
        """
        Envia mensagens de erro no Discord.

        Parameters

        kwargs:

        """

        show_traceback = kwargs.get('show_traceback', True)
        error_message = kwargs.get('error_message', '')
        log_level = kwargs.get('log_level', LOG_LEVELS['debug'])
        error_traceback = ''

        if show_traceback and traceback.format_exc() != 'NoneType: None\n':
            error_traceback = traceback.format_exc()

        if error_message:
            error_message = f' \n > **error_message**: {error_message}'

        error_traceback = f'{error_traceback}{error_message}'

        emoji = DATA_LOG[log_level]['emoji']
        title = DATA_LOG[log_level]['title']
        color = DATA_LOG[log_level]['color']

        params = {
            'wait': 'true',
        }

        payload = self.__generate_payload(color, emoji, error_traceback, title)

        if len(error_traceback) > 4096:

            if len(error_traceback) > 6000:
                error_traceback = '... ' + error_traceback[
                                           len(error_traceback) - 5996:len(
                                               error_traceback)]

            text_size = 4096
            embeds = []

            for index in range(0, len(error_traceback), text_size):

                if index == 0:
                    embeds.append(
                        {
                            'title': f'{emoji}{self.mode.upper()} - {title}',
                            'description': f'_ _ \n {error_traceback[index:index + text_size - 83]} ...',
                            'color': color
                        }
                    )
                    continue

                embeds.append(
                    {
                        'title': 'continuation',
                        'description': f'_ _ \n ... {error_traceback[index:index + text_size]}',
                        'color': color
                    }
                )

            payload['embeds'] = embeds

        try:
            response = httpx.post(self.webhook, params=params, json=payload)
            print(f'DISCORD_RESPONSE: {response.text}')
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
                    'color': color
                }
            ],
            'username': self.app_name,
            'avatar_url': self.avatar_url,
            'attachments': []
        }
        return payload


if __name__ == '__main__':
    log_discord = LogDiscord()
    try:
        25 / 0
        # raise 'ZeroDivisionError: division by zero'
    except ZeroDivisionError as error:
        log_discord.send(
            show_traceback=False,
            error_message='testando mensagem de erro',
            log_level=3
        )
