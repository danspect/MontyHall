import random
import sqlite3


class MontyHall:

    def __init__(self):
        self.conexao = sqlite3.connect("resultados.db")
        self.cursor = self.conexao.cursor()
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS monty_hall (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            ganhou_sem_trocar BOOLEAN, 
            ganhou_trocando BOOLEAN)""")

    @staticmethod
    def gen_random_door() -> int:
        """ Retorna um número aleatório entre 1 e 3. """
        return random.randint(1, 3)

    def monty_hall(self, trocar_porta: bool) -> bool:
        """ Cria um jogo de monty e retorna se o jogador ganhou ou não a partida. """
        porta_premiada: int = self.gen_random_door()
        primeira_porta_escolhida: int = self.gen_random_door()

        # Esta parte garante que a porta escolhida pelo apresentador
        # não será a porta escolhida pelo jogador nem a porta premiada.
        possiveis_portas_reveladas: int = {1, 2, 3} - {porta_premiada, primeira_porta_escolhida}
        porta_revelada: int = random.choice(list(possiveis_portas_reveladas))

        # Esta parte virifica se o jogador deve ou não trocar de porta.
        if trocar_porta:
            segunda_porta_escolhida: int = {1, 2, 3} - {porta_revelada, primeira_porta_escolhida}
            return segunda_porta_escolhida == porta_premiada
        else:
            return primeira_porta_escolhida == porta_premiada

    def save_to_db(self, ganhou_sem_trocar: bool, ganhou_trocando: bool) -> None:
        """ Salva os dados da partida em um banco de dados sqlite com três colunas. """
        # Insere os dados da partida na tabela.
        self.cursor.execute("INSERT INTO monty_hall (ganhou_sem_trocar, ganhou_trocando) VALUES (?, ?)",
                            (ganhou_sem_trocar, ganhou_trocando))

    def commit_changes(self) -> None:
        self.conexao.commit()

    def close_connection(self) -> None:
        self.conexao.close()

# Quantidade de partidas.
# Não é recomendado usar amostras muito grandes pois
# os dados ficam salvos na memoria.
amostra = 500_000

mh = MontyHall()
# Cria as partidas e salva os resultados no banco de dados.
for i in range(amostra):
    resultado_sem_trocar: bool = mh.monty_hall(False)
    resultado_trocando: bool = mh.monty_hall(True)
    mh.save_to_db(resultado_sem_trocar, resultado_trocando)

mh.commit_changes()
mh.close_connection()
