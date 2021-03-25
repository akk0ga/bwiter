import requests
from requests_oauthlib import OAuth1

# change with configUser
import config as ApiInfo


class Api:
    def __init__(self):
        """
         used to connect to twitter api
        """
        self.__api_key: str = ApiInfo.API_KEY
        self.__api_secret_key: str = ApiInfo.API_SECRET_KEY
        self.__bearer_token: str = ApiInfo.BEARER_TOKEN

    def __auth_oauth1(self):
        return OAuth1(client_key=self.__api_key, client_secret=self.__api_secret_key, resource_owner_key=)