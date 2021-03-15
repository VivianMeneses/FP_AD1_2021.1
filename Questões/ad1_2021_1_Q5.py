def conta_votos(lista_candidatos_numeros, lista_votos, numeros):
    brancos = 0
    nulos = 0
    contagem_geral = []
    for i in range(len(lista_candidatos_numeros)):
        contagem_individual = [lista_candidatos_numeros[i][0], 0]
        contagem_geral.append(contagem_individual)
    for v in votos:
        if v in numeros:
            for c in range(len(lista_candidatos_numeros)):
                if v == lista_candidatos_numeros[c][1]:
                    contagem_geral[c][1] += 1
        elif v == 0:
            brancos += 1
        else:
            nulos += 1

    print("Contagem geral: ", contagem_geral)
    print("Brancos: ", brancos)
    print("Nulos: ", nulos)




n = int(input())
cadidatos_numeros = []
numeros = []
for i in range(n):
    nome_numero = []
    x = input().split("#")
    nome_numero.append(x[0])
    nome_numero.append(int(x[1]))
    numeros.append(int(x[1]))
    cadidatos_numeros.append(nome_numero)
print(cadidatos_numeros)
voto = int(input())
votos = []
while voto >= 0:
    votos.append(voto)
    voto = int(input())
conta_votos(cadidatos_numeros, votos, numeros)

