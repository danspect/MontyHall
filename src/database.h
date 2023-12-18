#ifndef DATABASE_H
#define DATABASE_H

#include <sqlite3.h>
#include <stdbool.h>

typedef struct {
    sqlite3 *conexao;
    sqlite3_stmt *stmt;
} MontyHallDB;

void init_db(MontyHallDB *mh);
void save_to_db(MontyHallDB *mh, bool ganhou_sem_trocar, bool ganhou_trocando);
void commit_changes(MontyHallDB *mh);
void close_connection(MontyHallDB *mh);

#endif  // DATABASE_H