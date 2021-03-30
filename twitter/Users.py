from api.Api import Api


class Users(Api):
    """
    This class is create to get info from multiple __users
    """
    def get_users_list(self, limit: int, page: int, is_verified: bool) -> dict:
        """
        get lists of user
        :param limit: str
        :param page: str
        :param is_verified: bool
        :return:
        """
        query = self._input_query()
        user_list: dict = {}
        param: dict = {}

        # check if param declared
        if limit is not None:
            param['limit'] = limit
        if page is not None:
            param['page'] = page

        # call get request with correct param attribution
        if len(param) != 0:
            res = self._get(mod='user', sub_mod='list', query=query, param=param)
        else:
            res = self._get(mod='user', sub_mod='list', query=query)

        # stock data get
        for user in range(0, len(res)):
            if is_verified:
                if res[user]["verified"]:
                    user_list[res[user]["id_str"]] = {'name': res[user]["name"],
                                                      'id_name': res[user]['__screen_name'],
                                                      'desc': res[user]["description"]}

            else:
                user_list[res[user]["id_str"]] = {'name': res[user]["name"],
                                                  'id_name': res[user]['__screen_name'],
                                                  'desc': res[user]["description"]}
        return user_list
