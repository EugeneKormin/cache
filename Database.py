import redis


class Redis(object):
    def __init__(self):
        self.__redis = redis.Redis(host='localhost', port=6379, decode_responses=True)
        self.__account_names_set = "unique_account_names"
        self.__IS_EXISTS: bool

    def set(self, NAME: str):
        self.__redis.rpush("account_names", NAME)
        self.__redis.sadd(self.__account_names_set, NAME)
        # True

    def __find_name_in_cache(self, NAME: str):
        self.__IS_EXISTS = True if self.__redis.sismember("unique_account_names", NAME) == 1 else False

    def if_exists(self, NAME: str):
        self.__find_name_in_cache(NAME=NAME)
        return self.__IS_EXISTS
