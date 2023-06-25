# O Problema do Apresentador: Uma Abordagem Estatística para o Problema de Monty Hall

### Introdução

O problema de [Monty Hall](https://brilliant.org/wiki/monty-hall-problem/) envolve três portas, sendo que uma delas esconde um prêmio e as outras duas contém um bode. Uma pessoa (ou algum jogador) seleciona uma porta (que ainda não está aberta), e, logo após, outra porta (que não foi a escolhida) é aberta pelo apresentador e mostra que atrás desta havia um bode. Agora, restam duas portas fechadas (uma com o prêmio e outra com outro bode). Então, depois dessa etapa, a pessoa pode decidir se mantém a sua escolha inicial ou se troca de porta. A questão é: <strong> a melhor opção é ficar com a porta que escolheu no começo ou mudar para a outra porta que restou? </strong>

<img src="images/doors.png" alt="três portas com sinais de interrogação."/>

### O problema

Ao analisarmos os eventos possíveis, percebemos o seguinte: como a probabilidade de um evento ocorrer é dada pela razão dos casos favoráveis pelo total de casos, temos 1 caso favorável (escolher a porta com o prêmio) e três casos totais (as três portas), logo, podemos concluir que temos 1/3 de chance de ganhar ao escolher uma porta aleatória.

<img src="https://latex.codecogs.com/png.image?\inline&space;\large&space;\dpi{150}&space;{\color{White}&space;P&space;=&space;\frac{C_{F}}{C_{T}}}">
<p style="font-size: 70%" ><br/><em>Este conceito será melhor abordado quando solucionarmos o problema por meio da probabilidade. </em><br/></p>

Nesse sentido, o grande ponto do problema de Monty Hall é este: <strong> o apresentador deverá abrir uma das portas e revelar que nessa porta há um bode. </strong>

<img src="images/door-goat.png" alt="três portas: uma com uma cabra, duas com interrogações."/>

Por conseguinte, agora sabemos que uma das portas não tem nenhuma chance de ter o prêmio. Ou seja, é intuitivo pensar que agora cada uma das duas portas restantes possuem 50% de chance de ter o prêmio. No entanto, nos próximos tópicos será provado o porquê disso não ser verdade.  