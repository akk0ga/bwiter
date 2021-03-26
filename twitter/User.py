from api.Api import Api


class User(Api):
    def __init__(self):
        super().__init__()
        self.__api = Api()

    def get_users_list(self):
        """
        get lists of user
        :return:
        """
        query = self._input_query()
        user_list: dict = {}
        res = self.__api._get(mod='user', query=query)
        return res
