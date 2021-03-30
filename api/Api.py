import requests
from requests import exceptions as req_error
from requests_oauthlib import OAuth1
import urllib.parse as url_encode
import yaml


class Api:
    # load config file
    yml_file = open('config.yml', 'r')
    config = yaml.load(yml_file, Loader=yaml.FullLoader)
    yml_file.close()
    __API_KEY: str = config.get('API_KEY')
    __API_SECRET_KEY: str = config.get('API_SECRET_KEY')
    __ACCESS_TOKEN: str = config.get('ACCESS_TOKEN')
    __ACCESS_TOKEN_SECRET: str = config.get('ACCESS_TOKEN_SECRET')

    def __auth_oauth1(self) -> OAuth1:
        return OAuth1(client_key=self.__API_KEY, client_secret=self.__API_SECRET_KEY,
                      resource_owner_key=self.__ACCESS_TOKEN, resource_owner_secret=self.__ACCESS_TOKEN_SECRET)

    def _get(self, mod: str, sub_mod: str = None, query: str = None, param: dict = None) -> dict:
        """
        make get request and return response in json\n
        mod accept: 'tweet' or 'user'\n
        sub-mod accept: 'single' or 'list\n
        :param mod: str
        :param sub_mod: str
        :param query: str
        :param param: str
        :return:
        """
        try:
            # check which request execute
            if mod == 'user':
                if sub_mod == 'list':
                    url = f'https://api.twitter.com/1.1/users/search.json?q={query}&' \
                          f'count={param["limit"] if param is not None and param["limit"] else 20}&' \
                          f'page={param["page"] if param is not None and param["page"] else 1}'
                elif sub_mod == 'single':
                    url = f'https://api.twitter.com/1.1/users/show.json?user_id={param["user_id"]}&' \
                          f'__screen_name={param["__screen_name"]}'

                else:
                    raise Exception('sub_mod is not correct')
            elif mod == 'tweet':
                print(param['screen_name'])
                url = f'https://api.twitter.com/1.1/search/tweets.json?q=from%3A%40{param["screen_name"]}&' \
                      f'result_type=recent&count=1'
            else:
                raise Exception('please select mod')

            # execute request and return request result
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

    def get_rate_limit(self) -> dict:
        """
        check how much request are available
        :return:
        """
        url = 'https://api.twitter.com/1.1/application/rate_limit_status.json'
        req = requests.get(url=url, auth=self.__auth_oauth1())
        res = req.json()
        req.close()
        return res

    def _input_query(self) -> str:
        """
        input to get the get keyword
        :return:
        """
        query: input = input('enter keyword: ')
        print(query)
        while query == '' or len(query.split(' ')) > 10:
            query = input('Your query must be less than 10 keywords and be not empty: ')

        encode_query = url_encode.quote(query)
        return encode_query
