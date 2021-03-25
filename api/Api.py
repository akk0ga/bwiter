import requests

# change with configUser
import config as apiInfo


class Api:
    def __init__(self):
        """
         used to connect to twitter api
        """
        self.__api_key: str = apiInfo.API_KEY
        self.__api_secret_key: str = apiInfo.API_SECRET_KEY
        self.__bearer_token: str = apiInfo.BEARER_TOKEN
