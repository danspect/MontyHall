using System.Data;
using System.Reflection.Metadata;
using Microsoft.Data.Sqlite;

namespace MontyHall.Data;

public class DataContext : IDisposable
{
    private IDbConnection Connection { get; init; }
    private string databaseName = "MontyHall.db";
    private bool disposedValue;

    public DataContext()
    {
        Connection = CreateConnection();
        Connection.Open();
    }

    public IDbConnection CreateConnection()
    {
        return new SqliteConnection($"Data Source={databaseName}");
    }

    public void Init()
    {
        using var command = Connection.CreateCommand();
        command.CommandText = """
                CREATE TABLE IF NOT EXISTS MontyHall (
                    Id INTEGER PRIMARY KEY AUTOINCREMENT,
                    WonChanging INTEGER NOT NULL,
                    WonNotChanging INTEGER NOT NULL
                );
                """;
        var sqliteParameter = command.CreateParameter();

        command.ExecuteNonQuery();
    }

    public void AddGame(Model model)
    {
        using var transaticon = Connection.BeginTransaction();
        using var command = Connection.CreateCommand();
        command.CommandText = @"
            INSERT INTO MontyHall (WonChanging, WonNotChanging)
            VALUES ($wonChanging, $wonNotChanging)
            ";

        var changingParameter = command.CreateParameter();
        changingParameter.ParameterName = "$wonChanging";
        command.Parameters.Add(changingParameter);

        var notChangingParameter = command.CreateParameter();
        notChangingParameter.ParameterName = "$wonNotChanging";
        command.Parameters.Add(notChangingParameter);

        changingParameter.Value = model.wonChanging;
        notChangingParameter.Value = model.wonNotChanging;

        command.ExecuteNonQuery();
        transaticon.Commit();
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