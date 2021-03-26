import requests
from requests import exceptions as req_error
from requests_oauthlib import OAuth1
import urllib.parse as url_encode
# change config with configUser
import config as api_info


class Api:
    def __init__(self):
        """
         used for connect to twitter
         the rate is 900 request per minute
        """
        self.__API_KEY: str = api_info.API_KEY
        self.__API_SECRET_KEY: str = api_info.API_SECRET_KEY
        self.__BEARER_TOKEN: str = api_info.BEARER_TOKEN
        self.__ACCESS_TOKEN: str = api_info.ACCESS_TOKEN
        self.__ACCESS_TOKEN_SECRET: str = api_info.ACCESS_TOKEN_SECRET

    def __auth_oauth1(self) -> OAuth1:
        return OAuth1(client_key=self.__API_KEY, client_secret=self.__API_SECRET_KEY,
                      resource_owner_key=self.__ACCESS_TOKEN, resource_owner_secret=self.__ACCESS_TOKEN_SECRET)

    def get(self) -> object or str:
        """
        make get request and return json result
        :return:
        """
        try:
            search: str = input('enter your search: ')
            while search == '':
                search: str = input('enter your search: ')

            if len(search.split(' ')) > 10:
                raise Exception('the search is more than 10 keywords please reduce your search')

            # url = f'https://api.twitter.com/1.1/search/tweets.json?q={url_encode.quote(search)}'
            url = f'https://api.twitter.com/1.1/users/search.json?q={url_encode.quote(search)}&count=3'
            print(url)

            req = requests.get(url=url, auth=self.__auth_oauth1())
            res = req.json()
            print(res[1]['name'])
            return res
        except req_error.ConnectionError:
            print('Please check your connection: no connection')
        except req_error.Timeout:
            print('Request is timed out')
        except req_error.InvalidURL:
            print('Please check url: url is not valid')
        except req_error.HTTPError:
            print(f'An HTTP error occurred')
