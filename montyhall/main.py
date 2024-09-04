from database import Database, Game
from montyhallgame import MontyHallGame
from settings import amostra, db_name

db = Database(db_name)
mh = MontyHallGame()

for i in range(500):
    db.insert_data(Game(mh.monty_hall(True), mh.monty_hall(False)))

db.close_connection()
