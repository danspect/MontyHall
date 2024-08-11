from peewee import *
from models.game import *
from config.settings import db_name

class Database:

    def __init__(self, database_name: str) -> None:
        self.connection = SqliteDatabase(database_name)
        self.connection.connect()

    def commit_changes(self):
        self.connection.commit()

    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    database = Database(db_name)
    database.connection.create_tables([Game])
    _game = Game.create(1, 0, 1)