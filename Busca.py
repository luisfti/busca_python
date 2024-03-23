# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:11:31 2024

@author: Luis1
"""
#====IMPORTS==============================================================================

import random
import timeit
import time

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
        
    with open('./listas/aleatorio'+str(size)+'.txt', 'w') as a, open('./listas/aleatorio'+str(size*10)+'.txt', 'w') as b, open('./listas/aleatorio'+str(size*100)+'.txt', 'w') as c, open('./listas/aleatorio'+str(size*1000)+'.txt', 'w') as d:
        for x in entry1:
            line = str(x) + "\n"
            a.write(line)
            
        for x in entry2:
            line = str(x) + "\n"
            b.write(line)
            
        for x in entry3:
            line = str(x) + "\n"
            c.write(line)
            
        for x in entry1:
            line = str(x) + "\n"
            d.write(line)
    a.close(),b.close(),c.close(),d.close()
    
    
#====LEITURA============================================================================

# Função que le arquivos de listas  numéricas
def leitura(entry1,entry2,entry3,entry4,size):
    with open('./listas/aleatorio'+str(size)+'.txt') as a, open('./listas/aleatorio'+str(size*10)+'.txt') as b, open('./listas/aleatorio'+str(size*100)+'.txt') as c, open('./listas/aleatorio'+str(size*1000)+'.txt') as d:
        content_a = a.readlines()
        content_b = b.readlines()
        content_c = c.readlines()
        content_d = d.readlines()
        for x in content_a:
            entry1.append(int(x))
        for x in content_b:
            entry2.append(int(x))
        for x in content_c:
            entry3.append(int(x))
        for x in content_d:
            entry4.append(int(x))
    a.close(),b.close(),c.close(),d.close()
    
    
#====BUSCA==============================================================================

# Sequencial
def buscaSequencial(entry, key):
    for i in range(len(entry)):
        if entry[i] == key:
            return i
        time.sleep(0.0001)
    return -1

# Sequencial Ordenada
def buscaSequencialOrdenada(entry, key):
    for i in range(len(entry)):
        if entry[i] > key:
            return -1
        elif entry[i] == key:
            return i
        time.sleep(0.0001)

# Binária
def buscaBinaria(entry, key):
    start = 0
    end = len(entry)-1
    while start <= end:
        middle = (start + end)//2
        if entry[middle] == key:
            return middle
        elif entry[middle] < key:
            start = middle + 1
        elif entry[middle] > key:
                end = middle - 1
        time.sleep(0.0001)
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
    #aleatorio(entry1,entry2,entry3,entry4,size)

    # Le os arquivos com as entradas e poe nas listas
    leitura(entry1,entry2,entry3,entry4,size)
    
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
        print('Tempo: %.3fs' % (time1[i]))
        print("\n")
        
        
        # Ordena os itens da lista
        entry = sorted(entry)
        
        
        # Busca Sequencial ordenada ==================================
        print("SEQUENCIAL ORDENADA:")
        start = timeit.default_timer() # Contagem de tempo
        index = buscaSequencialOrdenada(entry, key)
        end = timeit.default_timer()
        time2.append(end - start)
        if(index != -1):
            print('Valor:', entry[index])
            print('Indice:', index)
        else:
            print('Valor:', key)
            print('Indice: não encontrado')
        print('Tempo: %.3fs' % (time1[i]))
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
        print('Tempo: %.3fs' % (time1[i]))
        print("\n")
        
    
    
    
if __name__ == "__main__":
    main()
    

