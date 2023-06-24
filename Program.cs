namespace MontyHall;

public class Program
{
    // Este valor que controla se o jogador deve ou não mudar de porta.
    private static bool trocarPorta = false;

    public static async Task SalvarResultados(string[] resultados, bool _trocarPorta)
        => await File.AppendAllLinesAsync($"resultados-{_trocarPorta}.csv", resultados);

    private static int CriarPorta()
        => new Random().Next(1, 3);

    /// <summary>
    ///     Esta função é o cérebro do jogo. Dependendo do experimento, podemos fazer o 
    ///  "jogador" trocar ou não de porta. 
    /// </summary>
    /// <param name="_trocarPorta"> Este parâmetro dita se o jogador vai trocar ou não de porta. </param>
    /// <returns> Retorna se o jogador ganhou ou não a partida. </returns>
    private static bool GerarPartida(bool _trocarPorta)
    {
        int portaPremiada = CriarPorta();
        int portaEscolhida = CriarPorta();
        int portaRevelada = CriarPorta();

        do
        {
            portaRevelada = CriarPorta();
        } while (portaRevelada == portaPremiada || portaRevelada == portaEscolhida);

        if (_trocarPorta)
        {
            do
            {
                portaEscolhida = CriarPorta();
            } while (portaEscolhida == portaPremiada || portaEscolhida == portaRevelada);
        }

        return portaEscolhida == portaPremiada;
    }

    public static async Task Main()
    {
        bool resultado;

        for (int i = 1; i <= 1000; i++)
        {
            resultado = GerarPartida(trocarPorta);
            //var partidasGanhas = possibilidades.Count(p => p.Item2 == "Ganhou");
            //var partidasPerdidas = possibilidades.Count(p => p.Item2 == "Perdeu");
            // double razao = (double)partidasGanhas / partidasPerdidas;
            // resultado[0] = "------------------------------------";
            // resultado[1] = $"Partidas ganhas: {partidasGanhas} \nPartidas perdidas: {partidasPerdidas} \nRazão: {razao}";
            string[] resultadosFormatado = new string[1];
            resultadosFormatado[0] = $"{i}, {resultado}"; 
            // Modelo para arquivo csv.


            // Console.WriteLine(resultado[1]);
            await SalvarResultados(resultadosFormatado, trocarPorta);
        }
    }
}
