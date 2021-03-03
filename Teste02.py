'''Escreva um algoritmo que obtenha 100 números inteiros de um usuário e os guarde em memória. Em seguida, leia esses valores da memória e conte quantas vezes cada número se repete. No final exiba uma lista com os números e o valor de repetições que cada um teve.'''

from random import randint

lista_numeros = []

if(len(lista_numeros) < 100):
    print('Sua lista não tem 100 elementos, iremos adicionar números randomicos entre 0 e 50')
    while(len(lista_numeros) < 100):
        lista_numeros.append(randint(0,50))
else:
    print('Sua lista está com 100 elementos, iremos prossegir')

lista_numeros.sort()
lista_numeros.append(1) #Número de corte

numeros_repetidos = []
repeticao = 0    
for i in range(len(lista_numeros)-1):
    if(lista_numeros[i] == lista_numeros[i+1]): #A ideia aqui é verificar se o próximo número é igual ao atual, ou seja, repetido
        repeticao = repeticao + 1
    else:
        numeros_repetidos.append([lista_numeros[i],repeticao + 1])
        repeticao = 0

#Testes
print(lista_numeros)
print(numeros_repetidos)  

for i in numeros_repetidos:
    print(f'Número {i[0]} aparece {i[1]} vezes')        





