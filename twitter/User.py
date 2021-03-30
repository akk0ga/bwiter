from twitter.Tweet import Tweet


class User(Tweet):
    def __init__(self):
        """
        This class is used to get info from single specified user
        """
        self.__screen_name: str

    def get_users_list(self, limit: int = None, page: int = None, is_verified: bool = False) -> dict:
        """
        get lists of user
        :param limit: str
        :param page: str
        :param is_verified: bool
        :return:
        """
        query = self._input_query()
        user_list: dict = {}
        param: dict = {}

        # check if param declared
        if limit is not None:
            param['limit'] = limit
        if page is not None:
            param['page'] = page

        # call get request with correct param attribution
        if len(param) != 0:
            res = self._get(mod='user', sub_mod='list', query=query, param=param)
        else:
            res = self._get(mod='user', sub_mod='list', query=query)

        # stock data get
        for user in range(0, len(res)):
            if is_verified:
                if res[user]["verified"]:
                    user_list[res[user]["id_str"]] = {'name': res[user]["name"],
                                                      'id_name': res[user]['__screen_name'],
                                                      'desc': res[user]["description"]}

            else:
                user_list[res[user]["id_str"]] = {'name': res[user]["name"],
                                                  'id_name': res[user]['__screen_name'],
                                                  'desc': res[user]["description"]}
        return user_list

    def get_user(self, user_id: str, screen_name: str) -> dict:
        """
        return single user
        :return:
        """
        res = self._get(mod='user', sub_mod='single', param={'user_id': user_id, '__screen_name': screen_name})
        user = {
            'general': {
                'id_str': res['id_str'],
                'name': res['name'],
                '__screen_name': res['__screen_name'],
                'desc': res['description'],
                'followers': res['followers_count'],
                'verified': res['verified'],
            },
            'image_info': {
                'has_pp': res['default_profile_image'],
                'has_banner': res['profile_use_background_image'],
                'profile_picture': res['profile_image_url_https'],
                'profile_banner': res['profile_banner_url']
            }
        }
        return user

    def last_tweet(self) -> dict:
        last_tweet = self._get_last_tweet(screen_name=self.__screen_name)

        # check if the tweet is new
        if last_tweet['status']:
            return {
                'new': True,
                'name': last_tweet['name'],
                'desc': last_tweet['desc'],
            }
        else:
            return{
                'new': False
            }

    """
    ============================
    getter setter
    ============================
    """
    def set_screen_name(self, new_screen_name: str):
        self.__screen_name = new_screen_name

    def get_screen_name(self):
        return self.__screen_name

    screen_name: property = property(fget=get_screen_name, fset=set_screen_name)
