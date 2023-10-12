<img src="https://logging-discord.readthedocs.io/en/latest/img/logo.png" width="200">

# Logging Discord
[![Documentation Status](https://readthedocs.org/projects/logging-discord/badge/?version=latest)](https://logging-discord.readthedocs.io/en/latest/?badge=latest)
[![CI](https://github.com/brunobrown/logging-discord/actions/workflows/pipeline.yml/badge.svg)](https://github.com/brunobrown/logging-discord/actions/workflows/pipeline.yml)
[![codecov](https://codecov.io/gh/brunobrown/logging-discord/graph/badge.svg?token=XTB97RAJA6)](https://codecov.io/gh/brunobrown/logging-discord)

- [English](README.md)
- [Português](README-pt.md)

O`Logging Discord` é uma ferramenta que facilita o registro de mensagens de erro em um canal no Discord. Ela permite o envio de mensagens de erro com informações personalizadas, como um traceback e mensagens específicas. Abaixo, você encontrará detalhes, parâmetros e métodos, bem como exemplos de uso.

## Índice

- [Parâmetros](#parâmetros)
- [Método `send`](#método-send)
- [Configuração via 'discord_config.py'](#configuração-via-discord_configpy)
- [Exemplos de Uso](#exemplos-de-uso)
- [Doações](#doações)

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

O método send é usado para enviar mensagens de erro para o canal no Discord.
Ele aceita os seguintes parâmetros:

* `show_traceback` (bool): Se True, exibe o traceback do erro na mensagem.
* `error_message` (str): Uma mensagem de erro personalizada a ser incluída na mensagem.
* `log_level` (int): Define o nível do log (0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical).

Exemplo de uso:

```python
logger.send(show_traceback=True, error_message="Erro crítico ocorreu!", log_level=5)
```

## Configuração via `discord_config.py`

Você pode configurar os parâmetros da classe `LogDiscord` criando um arquivo
chamado 'discord_config.py' na raiz do projeto. O arquivo 'discord_config.py'
deve conter as seguintes configurações:

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

---

## Doações

Obrigado por considerar apoiar o projeto! Sua ajuda é muito apreciada e me ajuda a continuar desenvolvendo e mantendo o software.

[Apoie o Projeto](https://logging-discord.readthedocs.io/en/latest/#support-the-project)