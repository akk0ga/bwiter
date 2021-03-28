from api.Api import Api


class Tweet(Api):

    def _get_last_tweet(self, screen_name: str) -> dict:
        """
        get las tweet for the specified user
        :param screen_name: str
        :return:
        """
        req: dict = self._get(mod='tweet', param={'screen_name': screen_name})
        res: dict = {
            'created_at': req['statuses'][0]['created_at'],
            'text': req['statuses'][0]['text'],
            'user_id_str': req['statuses'][0]['user']['id_str'],
            'name': req['statuses'][0]['user']['name'],
            'screen_name': req['statuses'][0]['user']['screen_name'],
        }
        return res
