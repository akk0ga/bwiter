from api.Api import Api
import json


class Tweet(Api):

    def _get_last_tweet(self, screen_name: str) -> dict:
        """
        get las tweet for the specified user
        :param screen_name: str
        :return:
        """
        def user_exist(req_username: str) -> bool:
            """
            check if user exist in json file
            :param req_username:
            :return:
            """
            file: dict = json.load(open('last_tweet.json', 'r'))
            for username in file:
                if username == req_username:
                    return True
            return False

        req: dict = self._get(mod='tweet', param={'screen_name': screen_name})
        req_screen_name = req['statuses'][0]['user']['screen_name']
        res: dict = {
            'tweet_id': req['statuses'][0]['id_str'],
            'created_at': req['statuses'][0]['created_at'],
            'text': req['statuses'][0]['text'],
            'user_id_str': req['statuses'][0]['user']['id_str'],
            'name': req['statuses'][0]['user']['name'],
            'screen_name': req['statuses'][0]['user']['screen_name'],
        }

        if user_exist(req_screen_name):
            # open json on read
            file = open('last_tweet.json', 'r')
            data: dict = json.load(file)
            file.close()

            # check if tweet is new
            if int(data[req_screen_name]['tweet_id']) < req['statuses'][0]['id']:
                data[req_screen_name] = res
                file = open('last_tweet.json', 'w')
                json.dump(data, file)
                file.close()
                return {
                    "status": True,
                    "name": res['name']
                }

            return {
                    "status": False,
                    "name": res['name']
                }
        else:
            new_data: dict = {req_screen_name: res}
            with open('last_tweet.json', 'r+') as file:
                data = json.load(file)
                data.update(new_data)
                file.seek(0)
                json.dump(data, file)
                file.close()
            return {
                    "status": True,
                    "name": res['name']
                }
