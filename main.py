import random

def gen_random_door() -> int:
    return random.randint(1, 3)

def monty_hall(trocar_porta: bool) -> bool:
    porta_premiada: int = gen_random_door()
    primeira_porta_escolhida: int = gen_random_door()

    while True:
        porta_revelada: int = gen_random_door()
        if porta_revelada == porta_premiada or porta_revelada == primeira_porta_escolhida:
            continue
        else:
            break

    if trocar_porta:
        while True:
            segunda_porta_escolhida: int = gen_random_door()
            if segunda_porta_escolhida == primeira_porta_escolhida or segunda_porta_escolhida == porta_revelada:
                continue
            else:
                break

    if trocar_porta:
        return True if segunda_porta_escolhida == porta_premiada else False
    else:
        return True if primeira_porta_escolhida == porta_premiada else False

def write_to_csv(texto: str, trocar_porta: bool) -> None:
    with open(f"resultados{trocar_porta}.csv", "a") as f:
        f.write(texto)
        f.close()

trocar_porta = True
for i in range(10000):
    resultado: bool = monty_hall(trocar_porta)
    resultado_formatado: str = f"{i}, {resultado}\n"
    write_to_csv(resultado_formatado, trocar_porta)
