#ifndef DATABASE_H
#define DATABASE_H

#include <sqlite3.h>
#include <stdbool.h>

typedef struct game
{
    bool ganhou_sem_trocar;
    bool ganhou_trocando;
} MontyHallGame;

typedef struct database
{
    sqlite3 *conexao;
    sqlite3_stmt *stmt;
} MontyHallDB;

void init_db(MontyHallDB *mh);
void save_to_db(MontyHallDB *database, MontyHallGame *game);
void commit_changes(MontyHallDB *mh);
void close_connection(MontyHallDB *mh);

#endif // DATABASE_H