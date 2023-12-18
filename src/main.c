#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>
#include "database.h"

int gen_random_door()
{
    return rand() % 3 + 1;
}

int main() 
{
    srand((unsigned)time(NULL));
    return 0;
}