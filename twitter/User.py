from twitter.Tweet import Tweet


class User(Tweet):
    __screen_name: str

    def __init__(self, screen_name: str):
        """
        This class is used to get info from single specified user
        """
        self.__screen_name: str = screen_name

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
