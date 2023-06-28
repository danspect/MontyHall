import random


def gen_random_door() -> int:
    ''' Retorna um número aleatório entre 1 e 3. '''
    return random.randint(1, 3)


def monty_hall(trocar_porta: bool) -> bool:
    ''' Cria um jogo de monty e retorna se o jogador ganhou ou não a partida. '''
    porta_premiada: int = gen_random_door()
    primeira_porta_escolhida: int = gen_random_door()

    # Esta parte garante que a porta escolhida pelo apresentador
    # não será a porta escolhida pelo jogador nem a porta premiada.
    while True:
        porta_revelada: int = gen_random_door()
        if porta_revelada == porta_premiada or porta_revelada == primeira_porta_escolhida:
            continue
        else:
            break

    # Esta parte virifica se o jogador deve ou não trocar de porta.
    if trocar_porta:
        while True:
            segunda_porta_escolhida: int = gen_random_door()
            if segunda_porta_escolhida == primeira_porta_escolhida or segunda_porta_escolhida == porta_revelada:
                continue
            else:
                return True if segunda_porta_escolhida == porta_premiada else False

    return True if primeira_porta_escolhida == porta_premiada else False


def write_to_csv(texto: str, trocar_porta: bool, range: int) -> None:
    ''' Escreve os dados da partida em um arquivo .csv. '''
    with open(f"resultados-{trocar_porta}-{range}.csv", "a") as f:
        f.write(texto)
        f.close()


trocar_porta = False
amostra = 10_000
write_to_csv("id, ganhou\n", trocar_porta, amostra)
for i in range(amostra):
    resultado: bool = monty_hall(trocar_porta)
    resultado_formatado: str = f"{i}, {resultado}\n"
    write_to_csv(resultado_formatado, trocar_porta, amostra)
