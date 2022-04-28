from aiohttp import web
from swimmy.frameworks.teams.app import APP
from swimmy.frameworks.slack.app import create_bot


if __name__ == "__main__":
    from .config import Config
    config = Config()
    if config.slack.get('bot_token'):
        try:
            create_bot()
        except Exception as error:
            raise error
    elif config.teams.get('app_id'):
        try:
            print(APP)
            web.run_app(APP, host="localhost", port=3978)
        except Exception as error:
            raise error
    else:
        raise Exception("Swimmy does not know which framework you are using. Please ensure you have provided the correct configuration file before proceeding.")
