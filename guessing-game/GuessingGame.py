from random import randint


class GuessingGame:
    def __init__(self):
        self.__upper_bound = None
        self.__lower_bound = None

    def __init__(self, a: int, b: int):
        self.__lower_bound = a
        self.__upper_bound = b

    def get_number(self):
        return randint(self.__lower_bound, self.__upper_bound)