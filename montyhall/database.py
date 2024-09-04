import sqlite3


class Game:
    def __init__(self, won_changing: bool, won_not_changing: bool) -> None:
        self.won_changing: int = 1 if won_changing else 0
        self.won_not_changing: int = 1 if won_not_changing else 0


class Database:

    def __init__(self, db_name: str) -> None:
        self.database_connection: sqlite3.Connection = sqlite3.connect(db_name)
        self.cursor: sqlite3.Cursor = self.database_connection.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS Game(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                won_changing INTEGER,
                                won_not_changing INTEGER
                            );"""
        )

    def insert_data(self, game: Game) -> None:
        self.cursor.execute(
            "INSERT INTO Game(won_changing, won_not_changing) VALUES (?, ?)",
            (game.won_changing, game.won_not_changing),
        )
        self.database_connection.commit()

    def get_all_games(self) -> list[tuple[int, int, int]]:
        result = self.cursor.execute("SELECT * FROM Game")
        return result.fetchall()

    def get_game_by_id(self, id: int) -> tuple[int, int]:
        result = self.cursor.execute(f"SELECT id FROM Game WHERE id == {id}")
        return result.fetchone()

    # def __enter__(self) -> sqlite3.Connection:
    #    self.database_connection = sqlite3.connect(self.db_name)
    #    return self.database_connection

    # def __exit__(self, exc_type, exc_value, traceback) -> None:
    #    self.database_connection.close()


if __name__ == "__main__":
    db = Database("test.db")

    for i in range(10):
        db.insert_data(Game(True, False))
    print(db.get_all_games())
