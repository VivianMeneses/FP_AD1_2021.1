import random
x = round(random.uniform(0,50),2)

l = 2
p = 3
lojas = []
produtos = []
produtos_limites = []
produtos_precos = []
lojas_geral = []

for k in range(l):
    print("Nome da loja ", k+1, ": ")
    lojas.append(input())

for i in range(p):
    produto_precos = []
    print("Digite os produtos e os limites:")
    texto = input().split()
    produto_precos.append(texto[0])
    produtos.append(texto[0])
    x = round(random.uniform(int(texto[1]),int(texto[2])),2)
    y = round(random.uniform(int(texto[1]),int(texto[2])),2)
    produto_precos.append(x)
    produto_precos.append(y)
    produtos_precos.append(produto_precos)

for n in range(len(lojas)):
    loja_produtos_precos = [lojas[n]]
    for m in range(p):
        loja_produtos_precos.append(produtos_precos[m][n+1])
    lojas_geral.append(loja_produtos_precos)

print("--------------------------")
print(lojas)
print(produtos_precos)
print("--------------------------")
print("Resultado da pesquisa:")
for produto in produtos:
    print("        ", end=" " )
    print(produto, end="  ")
print()
for m in (range(len(lojas_geral))):
    for i in range(len(lojas_geral[m])):
        print(lojas_geral[m][i], end="       ")
    print()
print()
total = 0
#for g in range(l):
#    for k in range(p)
#        if lojas_geral[g][k+1] == lojas_geral[g+1][k+1]

print("--------------------------")