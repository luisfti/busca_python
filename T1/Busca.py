# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:11:31 2024

@author: Luis1
"""
#====IMPORTS==============================================================================

import random
import time

#====CASO=================================================================================

# Função que gera um arquivo com uma lista de números aleatórios
def aleatorio(entry1,entry2,entry3,entry4,size):
    for i in range(size):
        x = random.randrange(1, 1001)
        if(x == 1000):
            x = 1
        entry1.append(x)
    
    for i in range(size*10):
        x = random.randrange(1, 1001)
        if(x == 1000):
            x = 1
        entry2.append(x)
        
    for i in range(size*100):
        x = random.randrange(1, 1001)
        if(x == 1000):
            x = 1
        entry3.append(x)
    
    for i in range(size*1000):
        x = random.randrange(1, 1001)
        if(x == 1000):
            x = 1
        entry4.append(x)
        
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
def busca_sequencial(entry, key):
    for i in range(len(entry)):
        if entry[i] == key:
            return i
        
    return -1

# Sequencial Ordenada
def busca_sequencial_ordenada(entry, key):
    for i in range(len(entry)):
        if i < len(entry)-1:
            if entry[i] < key and entry[i+1] > key:
                return -1
            elif entry[i] == key:
                return i
        else:
            if entry[i] == key:
                return i
            else:
                return -1
        
            
# Binária
def busca_binaria(entry, key):
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
        
    return -1

#====PRINT==============================================================================

# def plot_Values(index, time, key):
   


#====MAIN===============================================================================

def main():
    # Recupera o tamanho do vetor
    #size = int(input("Digite o tamanho da entrada:"))
    size = 10000
    
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
    
    # Cria um dicionário para armazenar as entradas
    entries = [entry1, entry2, entry3, entry4]
    tams = ["", "0", "00", "000"]
    
    # Faz um loop nos algoritmos de busca para cada entrada
    for i, entry in enumerate(entries):

        print("================"+str(size)+tams[i]+"=================")
        
        print("\n")
        # Busca Sequencial não ordenada ===============================
        print("SEQUENCIAL:")
        start = time.time() # Contagem de tempo
        index = busca_sequencial(entry, key)
        end = time.time()
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
        entry = sorted(entry)
        
        
        # Busca Sequencial ordenada ==================================
        print("SEQUENCIAL ORDENADA:")
        start = time.time() # Contagem de tempo
        index = busca_sequencial_ordenada(entry, key)
        end = time.time()
        time2.append(end - start)
        if(index != -1):
            print('Valor:', entry[index])
            print('Indice:', index)
        else:
            print('Valor:', key)
            print('Indice: não encontrado')
        print('Tempo: %.7fs' % (time2[i]))
        print("\n")

        
        # Busca Binária ordenada =====================================
        print("BINÁRIA:")
        start = time.time() # Contagem de tempo
        index = busca_binaria(entry, key)
        end = time.time()
        time3.append(end - start)
        if(index != -1):
            print('Valor:', entry[index])
            print('Indice:', index)
        else:
            print('Valor:', key)
            print('Indice: não encontrado')
        print('Tempo: %.7fs' % (time3[i]))
        print("\n")
        
    
    
    
if __name__ == "__main__":
    main()
    

