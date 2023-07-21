using System.Data;
using Dapper;
using Microsoft.Data.Sqlite;
using Microsoft.Extensions.Configuration;

namespace MontyHall.Data;

public class DataContext
{
    private readonly IConfiguration _configuration;

    public DataContext(IConfiguration configuration)
    {
        _configuration = configuration;
    }

    public IDbConnection CreateConnection()
    {
        return new SqliteConnection(_configuration.GetConnectionString("MontyHall"));
    }

    public async Task Init()
    {
        using (var connection = CreateConnection())
        {
            await _createMontyHallTable();

            async Task _createMontyHallTable()
            {
                var sql = """
                CREATE TABLE IF NOT EXISTS MontyHall (
                    Id BIGINT PRIMARY KEY AUTOINCREMENT,
                    GanhouTrocando INTEGER NOT NULL,
                    GanhouSemTrocar INTEGER NOT NULL
                );
                """;

                await connection.ExecuteAsync(sql);
            }
        }
    }
}