from api.Api import Api


class User(Api):
    def __init__(self):
        super().__init__()
        self.__api = Api()

    def get_users_list(self, limit: int = None, page: int = None) -> dict:
        """
        get lists of user
        :return:
        """
        query = self._input_query()
        user_list: dict = {}
        res = self.__api._get(mod='user', query=query, limit=limit, page=page)

        for user in range(0, len(res)):
            user_list[res[user]["id_str"]] = res[user]["name"]
        return user_list
