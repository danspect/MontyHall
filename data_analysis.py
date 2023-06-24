import  matplotlib.pyplot as plt

# Como estava na planiha, quando o jogador não trocou de porta
# ele ganhou 3.324 vezes.
sem_trocar: int = 3324
# Quando trocou, ele ganhou 6.693 vezes.
trocando: int = 6693

dados = [trocando, sem_trocar]

# Criando o gráfico de barras.
plt.bar(["trocar", "não trocar"], dados, color=["blue", "red"])
plt.title("Gráfico de barras")
plt.xlabel("Variáveis")
plt.ylabel("Valores")

# Salvando a imagem.
plt.savefig("grafico.png")