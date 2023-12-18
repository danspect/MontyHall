#include <sqlite3.h>
#include <stdbool.h>

typedef struct {
    sqlite3 *conexao;
    sqlite3_stmt *stmt;
} MontyHallDB;

void init_db(MontyHallDB *mh) {
    sqlite3_open("resultados.db", &mh->conexao);
    sqlite3_exec(mh->conexao,
        "CREATE TABLE IF NOT EXISTS monty_hall (id INTEGER PRIMARY KEY AUTOINCREMENT, ganhou_sem_trocar BOOLEAN, ganhou_trocando BOOLEAN)", 0, 0, 0);
    sqlite3_prepare_v2(mh->conexao,
        "INSERT INTO monty_hall (ganhou_sem_trocar, ganhou_trocando) VALUES (?, ?)",
        -1, &mh->stmt, 0);
}

void save_to_db(MontyHallDB *mh, bool ganhou_sem_trocar, bool ganhou_trocando) {
    sqlite3_bind_int(mh->stmt, 1, ganhou_sem_trocar);
    sqlite3_bind_int(mh->stmt, 2, ganhou_trocando);
    sqlite3_step(mh->stmt);
    sqlite3_reset(mh->stmt);
}

void commit_changes(MontyHallDB *mh) {
    sqlite3_exec(mh->conexao, "COMMIT", 0, 0, 0);
}

void close_connection(MontyHallDB *mh) {
    sqlite3_finalize(mh->stmt);
    sqlite3_close(mh->conexao);
}
