![Project Logo](
    img/logo.png
){ width='250px' .center }

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

## Como contribuir com o projeto?
Obrigado pelo interesse em contribuir com o projeto Logging Discord :heart:.

## Tests
Para os testes estamos usando o [pytest](https://pytest.org/). As configurações podem ser encontradas no 
arquivo [pyproject.toml](https://github.com/brunobrown/logging-discord/blob/master/pyproject.toml) na raiz do projeto.

Para as tarefas não listadas aqui, você pode consultar as [issues](https://github.com/brunobrown/logging-discord/issues).  

## Apoie o Projeto

Obrigado por considerar apoiar o projeto! Sua ajuda é muito apreciada e me
ajuda a continuar desenvolvendo e mantendo o software.

Existem duas maneiras de fazer doações:

### PIX

Se você preferir fazer uma doação via PIX:

   - [PIX ou QR Code](https://nubank.com.br/pagar/az4ws/snv4Ud3fJk)

![Nubank QR Code:](img/nubank_qrcode.png)

### Bitcoin

Aceito doações em Bitcoin. Se você deseja fazer uma doação em Bitcoin, use a
seguinte carteira:

- Bitcoin Wallet: 3QvDoHGUhYksbb9NkoEj7H45md48GXsnp6

![Bitcoin QR Code](img/bitcoin_qrcode.png)

Sua contribuição me ajuda a continuar aprimorando o projeto e oferecendo
suporte à comunidade de usuários. Agradeço pelo seu apoio!

!!! info "Sobre"
    Adicionar algo aqui