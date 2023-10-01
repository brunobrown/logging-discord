# Logging Discord

A classe `LogDiscord` é uma ferramenta que facilita o registro de mensagens de erro em um canal no Discord. Ela permite o envio de mensagens de erro com informações personalizadas, como um traceback e mensagens específicas. Abaixo, você encontrará detalhes sobre a classe, seus parâmetros e métodos, bem como exemplos de uso.

## Índice

- [Parâmetros](#parâmetros)
- [Método `send`](#método-send)
- [Método Privado `publish_record`](#método-privado-publish-record)
- [Método Privado `generate_embed_list`](#método-privado-generate-embed-list)
- [Método Privado `emove_extra_characters`](#método-privado-remove-extra-characters)
- [Método Privado `generate_payload`](#método-privado-generate-payload)
- [Configuração via 'discord_config.py'](#configuração-via-discord_configpy)
- [Exemplos de Uso](#exemplos-de-uso)

---

## Parâmetros

A classe `LogDiscord` possui os seguintes parâmetros em seu construtor:

- `webhook` (str): A URL do webhook do canal no Discord. Pode ser configurado no arquivo 'discord_config.py'.
- `avatar_url` (str): A URL do avatar a ser usado nas mensagens. Pode ser configurado no arquivo 'discord_config.py'.
- `mode` (str): O modo de desenvolvimento (e.g., "DEVELOPMENT", "HOMOLOGATION", "PRODUCTION"). Pode ser configurado no arquivo 'discord_config.py'.
- `app_name` (str): O nome do aplicativo que enviará as mensagens de erro. Pode ser configurado no arquivo 'discord_config.py'.
- `log_level` (int): Define o nível do log (0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical). Pode ser configurado no arquivo 'discord_config.py'.

Exemplo de uso:

```python
logger = LogDiscord()
```

---

## Método `send`

O método send é usado para enviar mensagens de erro para o canal no Discord. Ele aceita os seguintes parâmetros:

* `show_traceback` (bool): Se True, exibe o traceback do erro na mensagem.
* `error_message` (str): Uma mensagem de erro personalizada a ser incluída na mensagem.
* `log_level` (int): Define o nível do log (0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical).

Exemplo de uso:

```python
logger.send(show_traceback=True, error_message="Erro crítico ocorreu!", log_level=5)
```

---

## Método Privado `publish_record`

O método privado `__publish_record` é usado internamente para enviar o registro para o Discord. Não é necessário chamá-lo diretamente.

---

## Método Privado `generate_embed_list`

O método privado `__generate_embed_list` é usado internamente para gerar uma lista de incorporação (embeds) a serem incluídas na mensagem de erro. Ele aceita os seguintes parâmetros:

* `color` (str): A cor do texto.
* `emoji` (str): O emoji a ser exibido.
* `error_traceback` (str): O traceback do erro.
* `title` (str): O título do log.

Não é necessário chamá-lo diretamente.

---

## Método Privado `remove_extra_characters`

O método privado `__remove_extra_characters` é usado internamente para remover caracteres extras do traceback se seu comprimento exceder self.__number_characters.

Não é necessário chamá-lo diretamente.

---

## Método Privado `generate_payload`

O método privado `__generate_payload` é usado internamente para gerar a estrutura de payload que será enviada ao Discord. Ele aceita os seguintes parâmetros:

* `color` (str): A cor do texto.
* `emoji` (str): O emoji a ser exibido.
* `error_traceback` (str): O traceback do erro.
* `title` (str): O título do log.

Não é necessário chamá-lo diretamente.

---

## Configuração via `discord_config.py`

Você pode configurar os parâmetros da classe `LogDiscord` criando um arquivo chamado 'discord_config.py' na raiz do projeto. O arquivo 'discord_config.py' deve conter as seguintes configurações:

Exemplo:

```python
channel = {
    'webhook': 'https://discord.com/api/webhooks/example',
    'avatar_url': 'https://i0.wp.com/www.theterminatorfans.com/wp-content/uploads/2012/09/the-terminator3.jpg?resize=900%2C450&ssl=1',
    'mode': 'DEVELOPMENT',
    'app_name': 'APP_TEST',
}

log_levels = {
    #   color legend:
    #   * 2040357 = Black
    #   * 8947848 = Gray
    #   * 2196944 = Blue
    #   * 16497928 = Yellow
    #   * 14362664 = Red
    
    0: {
        'emoji': ':thinking:   ',
        'title': 'UNKNOWN ERROR',
        'color': 2040357,
    },
    1: {'emoji': ':bug:   ', 'title': 'DEBUG', 'color': 8947848},
    2: {
        'emoji': ':information_source:   ',
        'title': 'INFO',
        'color': 2196944,
    },
    3: {'emoji': ':warning:   ', 'title': 'WARNING', 'color': 16497928},
    4: {'emoji': ':x:   ', 'title': 'ERROR', 'color': 14362664},
    5: {'emoji': ':sos:   ', 'title': 'CRITICAL', 'color': 14362664},
}
```

---

## Exemplos de Uso

Aqui estão alguns exemplos de como usar a classe `LogDiscord`:

```python
# Criando uma instância do logger
logger = LogDiscord(webhook="sua_url_webhook", avatar_url="url_do_avatar", mode="DEVELOPMENT", app_name="MeuApp")

# Enviando um log de erro com traceback
logger.send(show_traceback=True, error_message="Erro crítico ocorreu!", log_level=5)

# Enviando um log de informação
logger.send(show_traceback=False, error_message="Operação bem-sucedida.", log_level=2)
```

#### Lembre-se de ajustar os parâmetros de acordo com suas necessidades e personalizar as mensagens de erro conforme necessário.