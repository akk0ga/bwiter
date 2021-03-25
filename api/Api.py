import requests
import config


class Api:
    def __init__(self):
        """
         used to connect to twitter api
        """
        self.__api_key: str = config.api_key
        self.__api_secret_key: str = config.api_secret_key
        self.__bearer_token: str = config.bearer_token
