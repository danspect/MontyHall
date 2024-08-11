from peewee import *

class Game(Model):

    def __init__(self, win_changing: int, win_not_changing: int, id: int) -> None:
        id = IntegerField
        win_changing = IntegerField()
        win_changing = IntegerField()