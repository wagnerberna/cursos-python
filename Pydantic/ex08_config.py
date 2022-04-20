from pydantic import BaseSettings, PostgresDsn, BaseModel
from typing import Literal, Union
import os
from dotenv import load_dotenv

load_dotenv()

# "postgresDns verifica se o formato do link com usuário e senha é válido."
class TestConfig(BaseSettings):
    env: Literal["test"]
    xpto: str = "MEU AMBIENTE DE TESTES"
    url_postgres: PostgresDsn


class ProdConfig(BaseSettings):
    env: Literal["prod"]
    gatinho: str = "MEU AMBIENTE DE GATINHO"


class DevConfig(BaseSettings):
    env: Literal["dev"]
    cachorrinho: str = "MEU AMBIENTE DE CACHORRO"


# UNION PARA ESCOLHER O AMBIENTE DE PRODUÇÃO
class Config(BaseModel):
    config: Union[DevConfig, TestConfig, ProdConfig]
