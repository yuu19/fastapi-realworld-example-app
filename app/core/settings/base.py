from enum import Enum

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"


class BaseAppSettings(BaseSettings):  
    model_config = SettingsConfigDict(
        env_file=".env",  # backendと同階層の.envファイルを読み込む
        env_ignore_empty=True,  # 環境変数が空の場合にエラーを発生させない
        extra="ignore",  # .envのみに存在する環境変数がある場合にエラーを発生させない
    )
    # app_env: AppEnvTypes = AppEnvTypes.prod
    app_env: AppEnvTypes = AppEnvTypes.dev
