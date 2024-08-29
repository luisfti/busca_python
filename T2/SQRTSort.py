# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 14:00:16 2024

@author: Luis1
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:11:31 2024

@author: Luis1
"""
#====IMPORTS==============================================================================

import math
import random
import time
import heapq

#====CASO=================================================================================

# Função que gera um arquivo com uma lista de números aleatórios
def aleatorio(entry1,entry2,entry3,entry4,size):
    
    # Cria as listas
    for i in range(size):
        x = random.randrange(1, 1000)
        entry1.append(x)
    
    for i in range(size*10):
        x = random.randrange(1, 1000)
        entry2.append(x)
        
    for i in range(size*100):
        x = random.randrange(1, 1000)
        entry3.append(x)
    
    for i in range(size*1000):
        x = random.randrange(1, 1000)
        entry4.append(x)
        
    
    # Cria os arquivos
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

# Função que le arquivos contendo listas  numéricas
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
    
    
#====MÉTODOS============================================================================

# Insertion Sort
def insertion_sort(arr):
    n = len(arr)
    max_val = arr[0]
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Insere o elemento na posição correta
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

        # Atualiza o máximo atual
        if key > max_val:
            max_val = key
    
    
    return max_val
        

#====ORDENAÇÃO==========================================================================

# Ordenação de raiz usando Insertion Sort
def sqrt_insertion_sort(arr):
    n = len(arr)
    block_size = int(math.sqrt(n))

    # Dividindo a lista em seções
    blocks = [arr[i:i+block_size] for i in range(0, n, block_size)]
   
    
    # Encontrando o máximo de cada seção usando insertion sort
    max_elements = [insertion_sort(section) for block in blocks]
   
    # Ordenando os máximos encontrados
    sorted_arr = []
    while max_elements:
        # Encontra o maior valor entre os máximos e adiciona à lista
        max_val = max(max_elements)
        sorted_arr.insert(0, max_val)
        
        
        # Remove o maior valor da seção correspondente
        max_index = max_elements.index(max_val)
        blocks[max_index].remove(max_val)
        
        # Atualiza o máximo daquela seção ou remove se estiver vazia
        if blocks[max_index]:
            max_elements[max_index] = insertion_sort(blocks[max_index])
        else:
            max_elements.pop(max_index)
            blocks.pop(max_index)
       

    return sorted_arr


# Ordenação de raiz usando Heap
def sqrt_heap_sort(arr):
    n = len(arr)
    block_size = int(math.sqrt(n))
    
    
    # Dividindo a lista em blocos
    blocks = [arr[i:i+block_size] for i in range(0, n, block_size)]
    
    # Construindo as heaps máximas de cada bloco
    block_heaps = []
    for block in blocks:
        heapq._heapify_max(block)  # Construtor
        block_heaps.append(block)
    

    # Construção da heap auxiliar 
    max_heap = []
    for i in range(len(block_heaps)):
        if block_heaps[i]:
            heapq.heappush(max_heap, (-block_heaps[i][0], i))
    

    # Ordenando os elementos
    sorted_arr = []
    while max_heap:
        max_value, block_index = heapq.heappop(max_heap)
        sorted_arr.insert(0, -max_value)  # Insere no início da lista para ordem crescente
        heapq._heappop_max(block_heaps[block_index])  # Remove o maior elemento do bloco
        if block_heaps[block_index]:  # Se ainda há elementos no bloco
            heapq.heappush(max_heap, (-block_heaps[block_index][0], block_index))
       
    return sorted_arr


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
    
    # Cria o arquivo com as entradas
    aleatorio(entry1,entry2,entry3,entry4,size)

    # Le os arquivos com as entradas e poe nas listas
    # leitura(entry1,entry2,entry3,entry4,size)
    
    
    # Cria um dicionário para armazenar as entradas
    entries = [entry1, entry2, entry3, entry4]
    tams = ["", "0", "00", "000"]
    
    # Faz um loop nos algoritmos de busca para cada entrada
    for i, entry in enumerate(entries):
        
        # print(entry)
        
        print("================"+str(size)+tams[i]+"=================")
        
        print("\n")
        # Insertion Sort ===============================
        print("SQRT - Insertion Sort:")
        start = time.time() # Contagem de tempo
        sorted_arr1 = sqrt_insertion_sort(entry)
        end = time.time()
        time1.append(end - start)
        
        print('Tempo de Ordenação: %.3fs' % (time1[i]))
        print("\n")
        
        
        
        # Heap Sort ==================================
        print("SQRT - Heap Sort:")
        start = time.time() # Contagem de tempo
        sorted_arr2 = sqrt_heap_sort(entry)
        end = time.time()
        time2.append(end - start)
    
        print('Tempo de Ordenação: %.3fs' % (time2[i]))
        print("\n")

        
    
if __name__ == "__main__":
    main()
    
