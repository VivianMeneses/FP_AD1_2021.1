#Importa a biblioteca
import math

#Fixando pi para três casas decimais
pi_fix = round((math.pi), 3)

km = 120000
#converte para centímetros
km_cm = km * 100000
d_cm = 50
#calcula o comprimento da roda
roda = 2*pi_fix*(d_cm/2)
#Decobre o número de rotações
n_rotacao = km_cm // roda

n = 0
m = 0

#Vai dividindo o número de rotações por 10 para descobrir o exponecial
while n_rotacao > 10:
    n_rotacao = n_rotacao/10
    m = n_rotacao
    n += 1

#Analisa se é maior que 3,16 para adicionar 1 ao exponencial
if m > 3.16:
    n += 1

km_f = format(km, ",d").replace(",",".")     
print(km_f)
print("Distância percorrida: ", km_f ," km")
print("Distância percorrida: ", km ," km")
print("Diâmetro da roda: ", d_cm, " cm")
print("Ordem de grandeza da quantidade de voltas efetuadas: 10 elevado a ", n)