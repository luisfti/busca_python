# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:11:31 2024

@author: Luis1
"""
#====IMPORTS==============================================================================

import random
import timeit
import heapq
import matplotlib.pyplot as plt


#====CASO=================================================================================

# Função que gera um arquivo com uma lista de números aleatórios
def aleatorio(entry1,entry2,entry3,entry4,size):
    
    for i in range(size):
        entry1.append(random.randrange(1, 1001))
    
    for i in range(size*10):
        entry2.append(random.randrange(1, 1001))
        
    for i in range(size*100):
        entry3.append(random.randrange(1, 1001))
    
    for i in range(size*1000):
        entry4.append(random.randrange(1, 1001))

    with open('aleatorio'+str(size)+'.txt', 'w') as arv:
        for i in entry1:    
            line = str(i) + "\n"
            arv.write(line)
    arv.close()
    
    with open('aleatorio'+str(size*10)+'.txt', 'w') as arv:
        for i in entry2:    
            line = str(i) + "\n"
            arv.write(line)
    arv.close()
    
    with open('aleatorio'+str(size*100)+'.txt', 'w') as arv:
        for i in entry3:    
            line = str(i) + "\n"
            arv.write(line)
    arv.close()
    
    with open('aleatorio'+str(size*1000)+'.txt', 'w') as arv:
        for i in entry4:    
            line = str(i) + "\n"
            arv.write(line)
    arv.close()
    

#====BUSCA==============================================================================

# Sequencial
def buscaSequencial(entry, key):
    for i in range(len(entry)):
        if entry[i] == key:
            return i
    return -1

# Binária
def buscaBinaria(entry, key):
    start = 0
    end = len(entry)-1
    while start <= end:
        middle = (start + end)//2
        if entry[middle] == key:
            return middle
        elif entry[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1


#====MAIN===============================================================================

def main():
    # Recupera o tamanho do vetor
    size = int(input("Digite o tamanho da entrada:"))
    
    # Listas de entradas não ordenada
    entry1 =[]
    entry2 =[]
    entry3 =[]
    entry4 =[]
    
    # Listas de tempo de execução
    time1 =[]
    time2 =[]
    time3 =[]
    
    # Cria o arquivo com as entradas
    aleatorio(entry1,entry2,entry3,entry4,size)
    
    # Adiciona a chave para busca
    key = int(input("Digite a chave para busca:"))
    print('\n')
    
    # Faz um loop nos algoritmos de busca para cada entrada
    for i in range(4):
        
        entry =[]
        tam = ""
        
        if (i == 0):
            entry = entry1
        elif(i == 1):
            entry = entry2
            tam ="0"
        elif(i == 2):
            entry = entry3
            tam ="00"
        else:
            entry = entry4
            tam ="000"
        
        print("================"+str(size)+tam+"=================")
        
        print("\n")
        # Busca Sequencial não ordenada ===============================
        print("SEQUENCIAL:")
        start = timeit.default_timer() # Contagem de tempo
        index = buscaSequencial(entry, key)
        end = timeit.default_timer()
        time1.append(end - start)
        if(index != -1):
            print('Valor:', entry[index])
            print('Indice:', index)
        else:
            print('Valor:', key)
            print('Indice: não encontrado')
        print('Tempo: %.7fs' % (time1[i]))
        print("\n")
        
        
        # Ordena os itens da lista
        heapq.heapify(entry1)
        
        
        # Busca Sequencial ordenada ==================================
        print("SEQUENCIAL ORDENADA:")
        start = timeit.default_timer() # Contagem de tempo
        index = buscaSequencial(entry, key)
        end = timeit.default_timer()
        time2.append(end - start)
        if(index != -1):
            print('Valor:', entry[index])
            print('Indice:', index)
        else:
            print('Valor:', key)
            print('Indice: não encontrado')
        print('Tempo: %.7fs' % (time1[i]))
        print("\n")

        
        # Busca Binária ordenada =====================================
        print("BINÁRIA:")
        start = timeit.default_timer() # Contagem de tempo
        index = buscaBinaria(entry, key)
        end = timeit.default_timer()
        time3.append(end - start)
        if(index != -1):
            print('Valor:', entry[index])
            print('Indice:', index)
        else:
            print('Valor:', key)
            print('Indice: não encontrado')
        print('Tempo: %.7fs' % (time1[i]))
        print("\n")
        
    
    
if __name__ == "__main__":
    main()
    

