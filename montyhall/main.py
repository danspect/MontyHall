from database import Database, Game
from data_analysis import plot
from montyhallgame import MontyHallGame
from settings import amostra, db_name

db = Database(db_name)
mh = MontyHallGame()

for i in range(amostra):
    print(f"Iteration: {i}", end='\r')
    db.insert_data(Game(mh.monty_hall(True), mh.monty_hall(False)))

data = db.get_all_games()

db.close_connection()

plot(data, "barchart.png")