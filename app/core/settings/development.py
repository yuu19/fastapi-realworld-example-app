import logging

from app.core.settings.app import AppSettings


# class DevAppSettings(AppSettings):
#     debug: bool = True

#     title: str = "Dev FastAPI example application"

#     logging_level: int = logging.DEBUG

#     # TODO[pydantic]: The `Config` class inherits from another class, please create the `model_config` manually.
#     # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
#     class Config(AppSettings.Config):
#         env_file = ".env"
class DevAppSettings(AppSettings):
    debug: bool = True
    title: str = "Dev FastAPI example application"
    logging_level: int = logging.DEBUG

    # AppSettings の model_config をコピーして、環境ファイルの設定を上書きする
    model_config = AppSettings.model_config.copy()
    model_config.update({"env_file": ".env"})