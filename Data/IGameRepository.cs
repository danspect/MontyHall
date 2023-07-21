namespace MontyHall.Data;

public interface IGameRepository
{ 
    Task AddGame(MontyHallResult result);

    Task<short[]> GetWins();

    Task<short[]> GetDefeats();
}
