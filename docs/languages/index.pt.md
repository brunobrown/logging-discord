![Project Logo](
    img/logging_discord.png
){ width='350px' .center }

# Logging Discord
Este projeto foi criado com o intuito de enviar para o Discord todo o traceback ou uma parte do mesmo junto a uma
mensagem de erro se necessário.

## Como instalar o pacote?
```bash
pip install logging_discord
```

## Como usar o pacote?
### Inicio rápido.

```python
{{ commands.import }}

log_discord = LogDiscord(webhook='https://webhook_do_seu_canal_no_discord')

log_discord.send(log_level=1)   # 0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical

```

## Configuração via `discord_config.py`

Você pode configurar os parâmetros da classe `LogDiscord` criando um arquivo
chamado 'discord_config.py' na raiz do projeto. O arquivo 'discord_config.py'
deve conter as seguintes configurações:

### Exemplo:

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

!!! info "Nota"
    Lembre-se de ajustar os parâmetros de acordo com suas necessidades e personalizar as mensagens de erro conforme necessário.

---

## Como contribuir com o projeto?

O projeto `Logging Discord` é de código aberto e recebe contribuições da comunidade. 
Se você deseja contribuir com melhorias, correções de bugs ou novos recursos, 
estou feliz em recebê-las. Abaixo estão as etapas básicas para começar a contribuir:

### 1. Ferramentas

Esse projeto basicamente usa duas ferramentas como base para todo com controle:

- [Poetry:](https://python-poetry.org/) Para o gerenciamento do ambiente e instalação de bibliotecas

- [Taskipy:](https://github.com/illBeRoy/taskipy) Para automação de tarefas rotineiras. Como executar os testes, linters, documentação e etc...

Então, garanta que tem o poetry instalado para essa contribuição:

[Como instalar o poetry](https://python-poetry.org/docs/#system-requirements)


### 2. Clonar o Repositório

Comece clonando o repositório do projeto:

```shell
git clone https://github.com/brunobrown/logging-discord.git
```

### 3. Instalar Dependências

Certifique-se de que você possui todas as dependências instaladas. 
Use o `poetry` para instalar as dependências necessárias:

```shell
poetry install
```

### 4. Criar um Ambiente Virtual (Opcional)

Recomendo criar um ambiente virtual para o desenvolvimento.

[Como criar um ambiente virtual](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)

```shell
poetry shell
```

### 5. Contribuir com Código

Faça as alterações que deseja e adicione ou modifique o código.

### 6. Testar as Alterações

Execute os testes para garantir que suas alterações não quebraram nada.

Para os testes estamos usando o [pytest](https://pytest.org/). As configurações
dele podem ser encontradas no arquivo [pyproject.toml](https://github.com/brunobrown/logging-discord/blob/master/pyproject.toml)
na raiz do projeto.

> Importante:
> 
> Os testes não estão apenas no `diretório logging-discord/tests`. 
A flag de `addopts = "--doctest-modules"` está sendo usada e caso modifique algo 
esteja ciente que as docstrings também rodam testes e são a base para documentação da API.

A cobertura de testes é gerada automaticamente com `pytest-cov` e são exibidas
quando a task de testes é executada:

```shell
task test
```
Os linters são requisitos para esses testes.

### 7. Criar um Pull Request

Após concluir suas alterações e testes, crie um Pull Request (PR) no repositório do projeto. 
Certifique-se de fornecer uma descrição clara do que suas alterações realizam e quais problemas elas resolvem.

### 8. Revisão e Mesclagem

Eu revisarei o seu PR e fornecerei feedback, se necessário. Uma vez aprovado, 
suas alterações serão mescladas no projeto principal.

### 9. Issues
Caso não tenha encontrado o que precisa, você pode abrir uma 
[issues](https://github.com/brunobrown/logging-discord/issues){ target="_blank" } no projeto 
relatando o que não consegue fazer ou o que precisa ser melhor documentado.

### 10. Agradeço a Sua Contribuição!

Obrigado pelo interesse em contribuir com o projeto `Logging Discord`, sua colaboração 
ajuda a melhorar o software para todos os usuários! :heart:

Se você tiver dúvidas ou precisar de assistência, entre em contato.

Estou ansioso para ver suas contribuições! &#128512;

---

## Apoie o Projeto

Obrigado por considerar apoiar o projeto! Sua ajuda é muito apreciada e me
ajuda a continuar desenvolvendo e mantendo o software.

Existem duas maneiras de fazer doações:

!!! info "PIX"

    Aceito doações via PIX:
    
    - [PIX ou QR Code](https://nubank.com.br/pagar/az4ws/snv4Ud3fJk){ target="_blank" }

    ![Nubank QR Code:](img/nubank_qrcode.png){ .center width="200px" }


!!! info "Bitcoin"

    Aceito doações em Bitcoin. Se você deseja fazer uma doação em Bitcoin, use a
    seguinte carteira:

    - Bitcoin Wallet: 3QvDoHGUhYksbb9NkoEj7H45md48GXsnp6

    ![Bitcoin QR Code](img/bitcoin_qrcode.png){ .center width="200px" }

Sua contribuição me ajuda a continuar aprimorando o projeto e oferecendo
    suporte à comunidade de usuários. Agradeço pelo seu apoio!

---

![Proverbios 16 3](img/proverbios_16_3.jpg){ .center width="500px" }

[Peça a Deus que abençoe os seus planos, e eles darão certo. Provérbios 16: 3](https://www.bible.com/bible/211/PRO.16.NTLH){ target="_blank" }
