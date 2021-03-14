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





# Questão 02

(ad1_2020_1_Q2)

Considere um DNA por uma sequência do alfabeto A, C, G, T, associando as bases nitrogenadas Adenina, Citosina, Guanina ou Timina, respectivamente. Considere também um motif por um intervalo de nucleotídeos (ou de aminoácidos, em proteínas) que possui alguma importância biológica. Queremos obter todas as substrings “mais próximas” do motif. Neste problema, “mais próxima” é definida pela distância de Hamming de duas substrings. 

<u>Definição:</u> Distância de Hamming entre duas strings de mesmo tamanho é o número de posições nas quais os caracteres das strings se diferem entre si. Exemplo: AGCT e CGCA possuem distância de Hamming igual a 2. 

**Entrada:** Um inteiro não negativo k, onde k ≤ 50 , uma string s de mofit, com no máximo 50 caracteres, e uma string t de DNA, com no máximo 500 caracteres. 

**Saída:** Todas substrings t′ de t tal que a distância de Hamming entre t′ e s seja no máximo k . Cada substring deve ser codificada na sua saída pela posição inicial em t seguida pelas posições onde t′ e s diferem. Se as entradas estiverem fora dos valores delimitados, então escreva "Valores não estão de acordo".

