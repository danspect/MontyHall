namespace MontyHall;

public class Program
{
    public static void Main()
    {
        var montyHall = new MontyHallStatistics();
        List<Tuple<int, string>> possibilidades;

        for (int i = 0; i < 100; i++)
        {
            possibilidades = montyHall.GerarPossibilidades();

            var partidasGanhas = possibilidades.Count(p => p.Item2 == "Ganhou");
            var partidasPerdidas = possibilidades.Count(p => p.Item2 == "Perdeu");
            double razao = (double)partidasGanhas / partidasPerdidas;

            //foreach (var possibilidade in possibilidades)
            //    Console.WriteLine(possibilidade);
            string[] resultado = new string[2];
            resultado[0] = "------------------------------------";
            resultado[1] = $"Partidas ganhas: {partidasGanhas} \nPartidas perdidas: {partidasPerdidas} \nRazão: {razao}";
            // resultado[0] = $"{i}, {partidasGanhas}, {partidasPerdidas}, {razao}"; // Modelo para arquivo csv.


            Console.WriteLine(resultado[1]);
            SalvarResultados(resultado);
        }
    }

    public static void SalvarResultados(string[] resultados)
    {
        File.AppendAllLines("resultados.txt", resultados);
    }
}
