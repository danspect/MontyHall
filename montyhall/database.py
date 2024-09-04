import sqlite3
from unittest import result


class Game:
    def __init__(self, won_changing: bool, won_not_changing: bool) -> None:
        self.won_changing: int = 1 if won_changing else 0
        self.won_not_changing: int = 1 if won_not_changing else 0


class Database:

    def __init__(self, db_name: str) -> None:
        self.db_name = db_name
        self.connection: sqlite3.Connection
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Game(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                won_changing INTEGER,
                                won_not_changing INTEGER
                            );"""
        )

    def insert_data(self, game: Game) -> None:
        self.cursor.execute(
            "INSERT INTO Game VALUES (?, ?)", (game.won_changing, game.won_not_changing)
        )
        self.connection.commit()

    def get_all_games(self) -> list[tuple[int, int, int]]:
        result = self.cursor.execute(
            "SELECT * FROM Game"
        )
        return result.fetchall()
    
    def get_game_by_id(self, id: int) -> tuple[int, int]:
        result = self.cursor.execute(f"SELECT id FROM Game WHERE id == {id}")
        return result.fetchone()

    def __enter__(self) -> sqlite3.Connection:
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self) -> None:
        self.connection.close()
