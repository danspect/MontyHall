import matplotlib.pyplot as plt
import sqlite3
import numpy as np


class ProjectDataAnalyser:

    def __init__(self):
        self.connection = sqlite3.connect("resultados.db")
        self.cursor = self.connection.cursor()

    def count_wins_changing(self) -> list[int, int]:
        """
        Retorna os dados de quand o jogador TROCA de porta
        [int, int] = [Vit., Der.]
        """
        resultados: list = []
        for trocar in [1, 0]:
            self.cursor.execute(f"""
                SELECT COUNT (*) FROM monty_hall WHERE ganhou_trocando == {trocar};
                """)
            resultados.append(self.cursor.fetchone())
        resultados = [x[0] for x in resultados]
        return resultados

    def count_wins_not_changing(self) -> list[int, int]:
        """
        Retorna os dados de quand o jogador NÃO troca de porta
        [int, int] = [Vit., Der.]
        """
        resultados: list = []
        for trocar in [1, 0]:
            self.cursor.execute(f"""
                SELECT COUNT (*) FROM monty_hall WHERE ganhou_sem_trocar == {trocar};
                """)
            resultados.append(self.cursor.fetchone())
        resultados = [x[0] for x in resultados]
        return resultados

    def close_connection(self) -> None:
        self.connection.close()


data = ProjectDataAnalyser()
trocando_porta = data.count_wins_changing()
sem_trocar = data.count_wins_not_changing()
data.close_connection()

troc_porta = trocando_porta[0] 
sem_troc = sem_trocar[0]

fig, ax = plt.subplots()
ax.bar(['Trocando', 'Não trocando'], [troc_porta, sem_troc], color=['blue', 'red'])
ax.set_ylabel('Vitorias (em milhões)')
ax.set_title('Vale a pena trocar de porta?')
plt.show()

plt.savefig("gráfico.png")