from src.services.SingletonClass import Singleton
import os
from dotenv import load_dotenv, find_dotenv

PY_ENV = ""
load_dotenv(find_dotenv())


@Singleton
class Config:
    """
     Clase para obtener variables de ambiente
     Al ser singleton, para llamar la clase se tiene que hacer de la siguiente
     manera: Config.instance().cualquier_metodo()
    """
    prefix = ''

    def __init__(self):
        if PY_ENV == 'production':
            self.prefix = 'PROD_'
        elif PY_ENV == 'staging':
            self.prefix = 'STAGING_'
        else:
            self.prefix = 'DEV_'
        load_dotenv(find_dotenv())

    def get_value(self, key):
        load_dotenv(find_dotenv())
        return os.getenv(self.prefix + key)
