from api.Api import Api


class Tweet(Api):

    def _get_last_tweet(self, screen_name: str) -> dict:
        """
        get las tweet for the specified user
        :param screen_name: str
        :return:
        """
        param: dict = {
            'screen_name': screen_name
        }
        res = self._get(mod='tweet', sub_mod='single', param=param)
        return res
