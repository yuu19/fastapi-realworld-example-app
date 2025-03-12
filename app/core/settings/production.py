# from app.core.settings.app import AppSettings


# class ProdAppSettings(AppSettings):
#     # TODO[pydantic]: The `Config` class inherits from another class, please create the `model_config` manually.
#     # Check https://docs.pydantic.dev/dev-v2/migration/#changes-to-config for more information.
#     class Config(AppSettings.Config):
#         env_file = "prod.env"

from app.core.settings.app import AppSettings

class ProdAppSettings(AppSettings):
    # 親の設定をコピーして上書き
    model_config = AppSettings.model_config.copy()
    model_config.update({"env_file": "prod.env"})