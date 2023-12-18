#include <sqlite3.h>
#include <stdbool.h>

typedef struct
{
    sqlite3 *conexao;
    sqlite3_stmt *stmt;
} MontyHallDB;

void init_db(MontyHallDB *database)
{
    sqlite3_open("resultados.db", &database->conexao);
    sqlite3_exec(database->conexao,
                 "CREATE TABLE IF NOT EXISTS monty_hall (id INTEGER PRIMARY KEY AUTOINCREMENT, ganhou_sem_trocar BOOLEAN, ganhou_trocando BOOLEAN)", 0, 0, 0);
    sqlite3_prepare_v2(database->conexao,
                       "INSERT INTO monty_hall (ganhou_sem_trocar, ganhou_trocando) VALUES (?, ?)",
                       -1, &database->stmt, 0);
}

void save_to_db(MontyHallDB *database, bool ganhou_sem_trocar, bool ganhou_trocando)
{
    sqlite3_bind_int(database->stmt, 1, ganhou_sem_trocar);
    sqlite3_bind_int(database->stmt, 2, ganhou_trocando);
    sqlite3_step(database->stmt);
    sqlite3_reset(database->stmt);
}

void commit_changes(MontyHallDB *database)
{
    sqlite3_exec(database->conexao, "COMMIT", 0, 0, 0);
}

void close_connection(MontyHallDB *database)
{
    sqlite3_finalize(database->stmt);
    sqlite3_close(database->conexao);
}
