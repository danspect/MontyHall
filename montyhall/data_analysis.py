import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def plot(data: list[tuple[int, int, int]]) -> None:
    df = pd.DataFrame(data, columns=["id", "win_changing", "win_not_changing"]).drop(columns=["id"])
    sb.barplot(df)
    plt.show()
