import requests
from requests import exceptions as req_error
from requests_oauthlib import OAuth1

# change config with configUser
import config as api_info


class Api:
    def __init__(self):
        """
         used for connect to twitter api
        """
        self.__API_KEY: str = api_info.API_KEY
        self.__API_SECRET_KEY: str = api_info.API_SECRET_KEY
        self.__BEARER_TOKEN: str = api_info.BEARER_TOKEN
        self.__ACCESS_TOKEN: str = api_info.ACCESS_TOKEN
        self.__ACCESS_TOKEN_SECRET: str = api_info.ACCESS_TOKEN_SECRET

    def __auth_oauth1(self) -> OAuth1:
        return OAuth1(client_key=self.__API_KEY, client_secret=self.__API_SECRET_KEY,
                      resource_owner_key=self.__ACCESS_TOKEN, resource_owner_secret=self.__ACCESS_TOKEN_SECRET)

    def get(self, url: str) -> object:
        """
        make get request and return json result
        :return:
        """
        try:
            res = requests.get(url=url, auth=self.__auth_oauth1())
            print(res.json())
            return res.json()
        except req_error.ConnectionError:
            print('Please check your connection: no connection')
        except req_error.Timeout:
            print('Request is timed out')
        except req_error.InvalidURL:
            print('Please check url: url is not valid')
        except req_error.HTTPError:
            print(f'An HTTP error occurred')
