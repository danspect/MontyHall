namespace MontyHall;

public class MontyHallStatistics
{
    public List<Tuple<int, string>> GerarPossibilidades()
    {
        var game = new MontyHallGame();
        var possibilidades = new List<Tuple<int, string>>();
        string resultado;

        for(int i = 1; i <= 1000; i++)
        {
            game.CriarPortas();
            resultado = game.Resultado();
            // Como interessa apenas saber se a troca tem uma maior 
            // chance de ganhar, consideramos o resultado fica como
            // "perdeu" e troca como "ganhou".
            possibilidades.Add(new Tuple<int, string>(i, resultado == "Troca" ? "Ganhou" : "Perdeu"));
        }

        return possibilidades;
    }
}

