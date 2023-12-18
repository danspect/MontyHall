#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include "database.h"

int gen_random_door()
{
    return rand() % 3 + 1;
}

bool monty_hall(bool trocar_porta)
{
    int porta_premiada = gen_random_door();
    int primeira_porta_escolhida = gen_random_door();

    int possiveis_portas_reveladas[2];
    int index = 0;

    for (int i = 1; i <= 3; ++i)
    {
        if (i != porta_premiada && i != primeira_porta_escolhida)
        {
            possiveis_portas_reveladas[index++] = i;
        }
    }

    int porta_revelada = possiveis_portas_reveladas[rand() % 2];

    if (trocar_porta)
    {
        int segunda_porta_escolhida = 6 - porta_revelada - primeira_porta_escolhida;
        return segunda_porta_escolhida == porta_premiada;
    }
    else
    {
        return primeira_porta_escolhida == porta_premiada;
    }
}

int main()
{
    srand((unsigned)time(NULL));
    int amostra = 500000;

    MontyHallDB mh;
    init_db(&mh);

    for (int i = 0; i < amostra; ++i)
    {
        bool resultado_sem_trocar = monty_hall(false);
        bool resultado_trocando = monty_hall(true);
        save_to_db(&mh, resultado_sem_trocar, resultado_trocando);
    }

    commit_changes(&mh);
    close_connection(&mh);

    return 0;
}