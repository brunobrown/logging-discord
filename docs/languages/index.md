![Project Logo](
    img/logging_discord.png
){ width='350px' .center }

# Logging Discord
This project was created with the purpose of sending the entire traceback or a portion of it along with an
error message to Discord if necessary.

## How to Install the Package?
```bash
pip install logging_discord

```

## How to Use the Package?
### Quick Start.

```python
{{ commands.import }}

log_discord = LogDiscord(webhook='https://your_discord_channel_webhook')

log_discord.send(log_level=1)   # 0 = unknown, 1 = debug, 2 = info, 3 = warning, 4 = error, 5 = critical
```

![error_message](img/error_message.png){ .center }

---

## Configuration with `discord_config.py`

You can configure the parameters of the LogDiscord class by creating a file
called 'discord_config.py' at the root of your project. The 'discord_config.py'
file should contain the following configurations:

### Exemple:

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

## Usage Examples

Here are some examples of how to use the `LogDiscord` class:

```python
# Creating a logger instance
logger = LogDiscord(webhook="your_webhook_url", avatar_url="avatar_url", mode="DEVELOPMENT", app_name="MyApp")

# Sending an error log with traceback
logger.send(show_traceback=True, error_message="Critical error occurred!", log_level=5)

# Sending an information log
logger.send(show_traceback=False, error_message="Operation successful.", log_level=2)
```

!!! info "Note"
    Remember to adjust the parameters according to your needs and customize error messages as necessary.

---

## How to Contribute to the Project

The `Logging Discord` project is open source and welcomes contributions from the community. 
If you want to contribute improvements, bug fixes, or new features, 
I'm happy to welcome them. Below are the basic steps to get started:

### 1. Tools

This project basically uses two tools as a base:

- [Poetry:](https://python-poetry.org/) For managing the environment and library installation.

- [Taskipy:](https://github.com/illBeRoy/taskipy) For automating routine tasks,
such as running tests, linters, documentation, etc.

So, ensure that you have Poetry installed for this contribution:

[How to install Poetry](https://python-poetry.org/docs/#system-requirements)

### 2. Clone the Repository

Start by cloning the project's repository:

```shell
git clone https://github.com/brunobrown/logging-discord.git
```

### 3. Install Dependencies

Make sure you have all the required dependencies installed. Use `poetry` 
to install the necessary dependencies:

```shell
poetry install
```

### 4. Create a Virtual Environment (Optional)

I recommend creating a virtual environment for development:

[How to create a virtual environment](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)

```shell
poetry shell
```

### 5. Contribute Code

Make the changes you want and add or modify the code.

### 6. Test Your Changes

Run the tests to ensure your changes haven't broken anything.

We use [pytest](https://pytest.org/) for testing, and its configuration can be found in the [pyproject.toml](https://github.com/brunobrown/logging-discord/blob/master/pyproject.toml) file at the project's root.

> Important:
> 
> Tests are not only in the `logging-discord/tests` directory. 
The `addopts = "--doctest-modules"` flag is used, and if you modify anything,
be aware that docstrings also run tests and serve as the basis for API documentation.

Test coverage is automatically generated with `pytest-cov` and is displayed when the test task is executed:

```shell
task test
```

### 7. Create a Pull Request

After completing your changes and tests, create a Pull Request (PR) in the 
project's repository. Be sure to provide a clear description of what your 
changes accomplish and which issues they resolve.

### 8. Review and Merge

I will review your PR and provide feedback if necessary. Once approved, your 
changes will be merged into the main project.

### 9. Issues
If you haven't found what you need, you can open an 
[issue](https://github.com/brunobrown/logging-discord/issues){ target="_blank" } 
in the project to report what you can't do or what needs better documentation.

### 10. Thank You for Your Contribution!

Thank you for your interest in contributing to the Logging Discord project. 
Your collaboration helps improve the software for all users! :heart:

If you have questions or need assistance, please feel free to reach out.

I look forward to seeing your contributions! &#128512;

---

## Support the Project

Thank you for considering supporting the project! Your help is greatly appreciated and it enables me
to continue developing and maintaining the software.

There are two ways to make donations:

!!! info "PIX"

    If you prefer to make a donation via PIX:

    - [PIX or QR Code](https://nubank.com.br/pagar/az4ws/AwolCAz0H1){ target="_blank" }

    ![Nubank QR Code:](img/nubank_qrcode.png){ .center width="200px"}


!!! info "Bitcoin"

    I accept donations in Bitcoin. If you wish to make a Bitcoin donation, please use the
    following wallet:

    - Bitcoin Wallet: 3QvDoHGUhYksbb9NkoEj7H45md48GXsnp6

    ![Bitcoin QR Code](img/bitcoin_qrcode.png){ .center width="200px" }


Your contribution helps me to keep improving the project and providing support to the user community. I appreciate your support!

---

![Proverbs 16 3](img/proverbs_16_3.jpg){ .center width="500px" }

[Commit your work to the LORD, and your plans will succeed. Proverbs 16: 3](https://www.bible.com/bible/116/PRO.16.NLT){ target="_blank" }

