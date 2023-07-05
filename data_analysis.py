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
troc_porta = data.count_wins_changing()
sem_troc = data.count_wins_not_changing()
data.close_connection()

# Agrupamento das barras.
x = ["Vitórias", "Derrotas"]

# Largura das barras.
width = 0.1

# Posições das barras.
x1 = np.arange(len(x))
x2 = x1 + width

# Criando o subplot.
fig, ax = plt.subplots()

# Desenhando as barras.
ax.bar(x1, troc_porta, width, label="Troc. porta", color="blue")
ax.bar(x2, sem_troc, width, label="Sem troc. porta", color="red")

# Adicionando os rótulos do eixo x.
ax.set_xticks(x2 + width / 2)
ax.set_xticklabels(x)

# Adicionando a legenda.
ax.legend()

# Salvando o gráfico.
plt.savefig("gráfico.png")