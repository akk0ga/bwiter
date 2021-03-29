from api.Api import Api
import json


class Tweet(Api):

    def _get_last_tweet(self, screen_name: str):
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

        # check if username already exist in json
        if user_exist(req['statuses'][0]['user']['screen_name']):
            print('yes')

        # check if new tweet
        """
        data = json.load(open('last_tweet.json', 'r'))
        if int(data['tweet_id']) < req['statuses'][0]['id']:
            # create json object
            res: dict = {
                'tweet_id': req['statuses'][0]['id_str'],
                'created_at': req['statuses'][0]['created_at'],
                'text': req['statuses'][0]['text'],
                'user_id_str': req['statuses'][0]['user']['id_str'],
                'name': req['statuses'][0]['user']['name'],
                'screen_name': req['statuses'][0]['user']['screen_name'],
            }
            # override previous data in json
            with open('twitter/last_tweet.json', 'w') as file:
                json.dump(res, file)
                file.close()
            return res
        """