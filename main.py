import random


class Montyhall():

    def gen_random_door(self) -> int:
        return random.randint(1, 3)

    def monty_hall(self, trocar_porta: bool) -> bool:
        porta_premiada: int = self.gen_random_door()
        primeira_porta_escolhida: int = self.gen_random_door()
        possiveis_portas_reveladas: int = {1, 2, 3} - {porta_premiada, primeira_porta_escolhida}
        porta_revelada: int = random.choice(list(possiveis_portas_reveladas))
        if trocar_porta:
            segunda_porta_escolhida: int = {1, 2, 3} - {porta_revelada, primeira_porta_escolhida}
            return segunda_porta_escolhida == porta_premiada
        else:
            return primeira_porta_escolhida == porta_premiada
