from api.Api import Api
import json


class Tweet(Api):

    def _get_last_tweet(self, screen_name: str) -> dict:
        """
        get las tweet for the specified user
        :param screen_name: str
        :return:
        """
        req: dict = self._get(mod='tweet', param={'screen_name': screen_name})

        # check if new tweet
        data = json.load(open('twitter/last_tweet.json', 'r'))
        if int(data['tweet_id']) < req['statuses'][0]['id']:
            # crate json object
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
