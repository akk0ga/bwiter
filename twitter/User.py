from api.Api import Api


class User(Api):
    def __init__(self):
        super().__init__()
        self.__api = Api()

    def get_users_list(self, limit: int = None, page: int = None, is_verified: bool = False) -> dict:
        """
        get lists of user
        :param limit: str
        :param page: str
        :param is_verified: bool
        :return:
        """
        query = self._input_query()
        user_list: dict = {}
        res = self.__api._get(mod='user', sub_mod='list', query=query, limit=limit, page=page)

        for user in range(0, len(res)):
            if is_verified:
                if res[user]["verified"]:
                    user_list[res[user]["id_str"]] = {'name': res[user]["name"],
                                                      'id_name': res[user]['screen_name'],
                                                      'desc': res[user]["description"]}
            else:
                user_list[res[user]["id_str"]] = {'name': res[user]["name"],
                                                  'id_name': res[user]['screen_name'],
                                                  'desc': res[user]["description"]}
        return user_list

    def get_user(self) -> dict:
        """
        return single user
        :return:
        """
        query = self._input_query()
        user: dict = {}
        res = self.__api._get(mod='user', sub_mod='list', query=query)
        print(res)
        return user
