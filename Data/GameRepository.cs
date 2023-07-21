using Dapper;

namespace MontyHall.Data;

public class GameRepository : IGameRepository
{
    private readonly DataContext _context;

    public GameRepository(DataContext context)
    {
        _context = context;
    }

    public async Task AddGame(MontyHallResult result)
    {
        using(var connection = _context.CreateConnection())
        {
            var sql = @"
            INSERT INTO MontyHall (GanhouTrocando, GanhouSemTrocar)
            VALUES (@wonChanging, @wonNotChanging)
            ";

            await connection.ExecuteAsync(sql, result);
        }
    }

    public Task<short[]> GetDefeats()
    {
        using(var connection = _context.CreateConnection())
        {
            var sql = @"
            SELECT COUNT (*) FROM MontyHall WHERE GanhouTrocando == 1;
            SELECT COUNT (*) FROM MontyHall WHERE GanhouSemTrocar == 1;
            ";

            var result = connection.QueryMultipleAsync(sql); 
        }
    }

    public Task<short[]> GetWins()
    {
        throw new NotImplementedException();
    }
}
