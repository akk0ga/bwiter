from api.Api import Api


class Tweet(Api):

    def _get_last_tweet(self, screen_name: str) -> dict:
        """
        get las tweet for the specified user
        :param screen_name: str
        :return:
        """
        res = self._get(mod='tweet', sub_mod='single', param={'screen_name': screen_name})
        return res
