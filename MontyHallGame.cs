namespace MontyHall;

class MontyHallGame
{
    private int portaPremiada; // a porta que contém o prêmio.
    private int portaEscolhida; // a porta que o jogador escolheu.
    private int portaRevelada; // a porta que o apresentador abriu.

    public MontyHallGame()
    {
        // Escolhe qual vai ser a porta premiada.
        portaPremiada = new Random().Next(1, 3);

        // Escolhe uma porta.
        portaEscolhida = new Random().Next(1, 3);

        // Abre uma porta.
        portaRevelada = new[] { 1, 2, 3 }.Except(new[] { portaEscolhida, portaPremiada }).First();
        // Note que a função except faz com que a porta revelada .
        // não seja a porta escolhida pelo usuário ou a porta.
        // que contém o prêmio.
    }

    public string Resultado()
    {
        // Se a porta com o prêmio for a mesma que o jogador escolheu,
        // o resultado é fica.
        // Se não for, o resultado é troca.
        string resultado = portaPremiada == portaEscolhida ? "Fica" : "Troca";

        return resultado;
    }
}