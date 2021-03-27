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

    def _get(self, mod: str, query: str, limit: int = None, page: int = None) -> dict:
        """
        make get request and return response in json,
        mod accept 'tweet' / 'user'
        :param mod: str
        :return:
        """
        try:
            if mod == 'user':
                url = f'https://api.twitter.com/1.1/users/search.json?q={query}&' \
                      f'count={limit if limit is not None else 20}&page={page if page is not None else 1}'
                print(url)
            else:
                return {}

            req = requests.get(url=url, auth=self.__auth_oauth1())
            res = req.json()
            req.close()
            return res
        except req_error.ConnectionError:
            print('Please check your connection: no connection')
        except req_error.Timeout:
            print('Request is timed out')
        except req_error.InvalidURL:
            print('Please check url: url is not valid')
        except req_error.HTTPError:
            print(f'An HTTP error occurred')

    def _input_query(self) -> str:
        """
        input to get the get keyword
        :return:
        """
        query: input = input('enter keyword: ')
        print(query)
        while query == '' or len(query.split(' ')) > 10:
            print(query)
            print(query.split(' '))
            query = input('Your query must be less than 10 keywords and be not empty: ')

        encode_query = url_encode.quote(query)
        return encode_query
