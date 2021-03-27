from api.Api import Api


class Tweet(Api):

    def get_last(self, user_screen_name: str, ) -> dict:
        query = f'from:{user_screen_name}'
        res = self._get(mod='tweet', sub_mod='single', query=query)
        return res
