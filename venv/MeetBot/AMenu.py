from abc import ABC, abstractmethod

class AMenu(ABC):

    def __init__(self, filter, name):
        self.filter = filter
        self.name = name
        self.buttons_dict = dict()

