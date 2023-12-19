using System.Data;
using Dapper;
using Microsoft.Data.Sqlite;
using Microsoft.Extensions.Configuration;

namespace MontyHall.Data;

public class DataContext : IDisposable
{
    private IDbConnection Connection { get; init; }
    private string databaseName = "MontyHall.db";
    private bool disposedValue;

    public DataContext()
    {
        Connection = CreateConnection();
    }

    public IDbConnection CreateConnection()
    {
        return new SqliteConnection($"Data Source={databaseName}");
    }

    public async Task Init()
    {
        await _createMontyHallTable();

        async Task _createMontyHallTable()
        {
            var sql = """
                CREATE TABLE IF NOT EXISTS MontyHall (
                    Id BIGINT PRIMARY KEY AUTOINCREMENT,
                    WonChanging INTEGER NOT NULL,
                    WonNotChanging INTEGER NOT NULL
                );
                """;

            await Connection.ExecuteAsync(sql);
        }
    }

    public async Task AddGame(Model model)
    {
        var sql = @"
            INSERT INTO MontyHall (GanhouTrocando, GanhouSemTrocar)
            VALUES (@wonChanging, @wonNotChanging)
            ";

        await Connection.ExecuteAsync(sql, model);
    }

    protected virtual void Dispose(bool disposing)
    {
        if (!disposedValue)
        {
            if (disposing)
            {
                // TODO: dispose managed state (managed objects)
                Connection.Close();
                Connection.Dispose();
            }

            // TODO: free unmanaged resources (unmanaged objects) and override finalizer
            // TODO: set large fields to null
            disposedValue = true;
        }
    }

    // // TODO: override finalizer only if 'Dispose(bool disposing)' has code to free unmanaged resources
    // ~DataContext()
    // {
    //     // Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
    //     Dispose(disposing: false);
    // }

    public void Dispose()
    {
        // Do not change this code. Put cleanup code in 'Dispose(bool disposing)' method
        Dispose(disposing: true);
        GC.SuppressFinalize(this);
    }
}