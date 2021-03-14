# AD1-Fundamentos-de-Programação
:computer: AD1 de Fundamentos da Programação de 2021.1

## Questão 01

(ad1_2020_1_Q1)

No painel de um carro, está indicado no hodômetro a distância, em km , que o carro “rodou”. Faça um programa que escreva a ordem de grandeza do número de voltas efetuadas pela roda desse carro, sabendo o valor do diâmetro da roda, em cm : 

* Obs 1: Despreze possíveis derrapagens e frenagens do carro. 

* Obs 2: O comprimento da roda é igual a 2πR , onde R é o valor do raio da roda do carro. 

* Obs 3: Utilize π importado do módulo math e adote π com apenas três casas decimais. 

* Obs 4: A ordem de grandeza de um número é a potência de 10 mais próxima deste número. Assim, dado X um número escrito na notação científica, X = m.10 , onde e n 1 ≤ m < 10 n ∈ Z, a ordem de grandeza de X será: 10 , se , ou , caso contrário. n m < 3, 16 10 n+1 

Entrada: Dois inteiros. O primeiro indica a distância percorrida pelo carro, em km , e o segundo indica o diâmetro da roda do carro, em cm . 

Saída: Ordem de grandeza do número de voltas efetuadas pela roda deste carro.

![Alt text](https://github.com/VivianMeneses/FP_AD1_2021.1/blob/main/img/Q1_img_saida.PNG?raw=true "Optional title")



# Questão 02

(ad1_2020_1_Q2)

Considere um DNA por uma sequência do alfabeto A, C, G, T, associando as bases nitrogenadas Adenina, Citosina, Guanina ou Timina, respectivamente. Considere também um motif por um intervalo de nucleotídeos (ou de aminoácidos, em proteínas) que possui alguma importância biológica. Queremos obter todas as substrings “mais próximas” do motif. Neste problema, “mais próxima” é definida pela distância de Hamming de duas substrings. 

<u>Definição:</u> Distância de Hamming entre duas strings de mesmo tamanho é o número de posições nas quais os caracteres das strings se diferem entre si. Exemplo: AGCT e CGCA possuem distância de Hamming igual a 2. 

**Entrada:** Um inteiro não negativo k, onde k ≤ 50 , uma string s de mofit, com no máximo 50 caracteres, e uma string t de DNA, com no máximo 500 caracteres. 

**Saída:** Todas substrings t′ de t tal que a distância de Hamming entre t′ e s seja no máximo k . Cada substring deve ser codificada na sua saída pela posição inicial em t seguida pelas posições onde t′ e s diferem. Se as entradas estiverem fora dos valores delimitados, então escreva "Valores não estão de acordo".

![Alt text](https://github.com/VivianMeneses/FP_AD1_2021.1/blob/main/img/Q2_img_saida.PNG?raw=true "Optional title")



# Questão 03

(ad1_2020_1_Q3)

Sr Cederjeano notou que estava engordando muito durante a pandemia e decidiu entrar para a academia. Assim, Sr Cederjeano precisa comprar equipamentos para sua malhação e vai, primeiramente, em algumas lojas pesquisar os preços desses equipamentos. Faça um programa que receba como entrada um inteiro L , um inteiro P , ambos não nulos, L nomes associando às lojas pesquisadas, P nomes associando aos produtos pesquisados nas lojas, e para cada produto, receba dois inteiros não negativos a e b , onde a ≤ b , que delimitarão os valores mínimo e máximo de cada produto nas lojas. Construa uma matriz bidimensional LxP com as dimensões lidas e com valores gerados aleatoriamente, com duas casas decimais, importada do módulo random . 

**Escreva:**

1. A matriz com os valores, incluindo, também, os nomes das lojas e produtos nos índices das linhas e colunas, respectivamente; 
2. Exiba por linha o par produto e loja com menores preço; 
3. Exiba o total a ser gasto ao considerar os menores preços.

![Alt text](https://github.com/VivianMeneses/FP_AD1_2021.1/blob/main/img/Q3_img_saida.PNG?raw=true "Optional title")



# Questão 04

(ad1_2020_1_Q4)

Faça um programa, contendo subprogramas, que leia linhas da entrada padrão até que uma linha vazia seja digitada. Com exceção da linha vazia, todas as anteriores contém um par de números inteiros, representando a coordenada x e y de um ponto no espaço bidimensional. Calcule e escreva o centro geométrico, ou ponto centróide, de todos os pontos lidos. A coordenada x do centróide é dada pela média de todos os x’s lidos. Assim como a sua coordenada y é dada pela média de todos os y’s lidos. Em seguida, escreva na saída padrão o ponto mais próximo e o ponto mais distante do centróide. Caso nenhum ponto seja digitado, escreva a mensagem: “Nenhum ponto lido. Portanto, não há centróide!!!”. 

<u>Definição:</u> a distância entre dois pontos (xA,yA) e (xB,yB) é dada pela raiz quadrada da soma do quadrado das diferenças (xB-xA) e (yB-yA).

![Alt text](https://github.com/VivianMeneses/FP_AD1_2021.1/blob/main/img/Q4_img_saida.PNG?raw=true "Optional title")

# Questão 05

(ad1_2020_1_Q5)

Faça um programa, contendo subprogramas, que leia inicialmente a contagem de candidatos em uma eleição. Em seguida, em cada linha, leia o nome de um dos candidatos e seu respectivo número positivo, separados por um #. Utilize uma estrutura de dados para manter estas informações. Em seguida, leia números representando votos da eleição. Um voto por linha lida, até que um número negativo seja digitado. Totalize e escreva na saída padrão os votos de cada candidato, suponha que o número zero represente um voto em branco e um número positivo que não pertença a nenhum dos candidatos seja um voto nulo. Ao final, também escreva quantos foram os votos em branco e quantos foram os votos nulos.

![Alt text](https://github.com/VivianMeneses/FP_AD1_2021.1/blob/main/img/Q5_img_saida.PNG?raw=true "Optional title")



# Questão 06

(ad1_2020_1_Q6)

Faça um programa, contendo subprograma, que leia strings da entrada padrão até que uma string vazia seja digitada. Faça e utilize uma função recursiva que analise se a string lida é uma palíndrome. Toda string palíndrome deve ser escrita na saída padrão. 

<u>Definição:</u> uma string é palíndrome se e somente se o primeiro caractere é igual ao último, o segundo caractere é igual ao penúltimo, e assim sucessivamente.

![Alt text](https://github.com/VivianMeneses/FP_AD1_2021.1/blob/main/img/Q6_img_saida.PNG?raw=true "Optional title")