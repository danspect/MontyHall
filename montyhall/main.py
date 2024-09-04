import os
from data_analysis import plot
from database import Database, Game
from jinja2 import Environment, FileSystemLoader
from montyhallgame import MontyHallGame
from settings import amostra, db_name


env = Environment(loader=FileSystemLoader(searchpath=(os.path.join(os.path.realpath(os.path.dirname(__file__)), "templates"))))
template = env.get_template("data.html")

db = Database(db_name)
mh = MontyHallGame()

for i in range(amostra):
    print(f"Iteration: {i}", end="\r")
    db.insert_data(Game(mh.monty_hall(True), mh.monty_hall(False)))

wins: dict[str, tuple[int, None]] = {
    "changing": db.get_wins_changing(),
    "not_changing": db.get_wins_not_changing(),
}

ratio: float = wins["changing"][0] / wins["not_changing"][0]

data = db.get_all_games()

db.close_connection()

plot(data, "barchart.png")

rendered_html = template.render(
    wins_changing=wins["changing"][0], wins_not_changing=wins["not_changing"][0], ratio=ratio
)

with open("final_analysis.html", "w") as f:
    f.write(rendered_html)
