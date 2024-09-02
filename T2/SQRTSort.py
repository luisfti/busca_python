import os
import math
import random
import time
import heapq

#====CASO=================================================================================

# Função que gera uma lista de números aleatórios e salva em um arquivo
def gerar_entrada(size):
    # Cria diretório se não existir
    if not os.path.exists('./listas'):
        os.makedirs('./listas')
    
    # Gera lista de números aleatórios
    entry = [random.randrange(1, 10000) for _ in range(size)]
    
    # Salva a lista em um arquivo
    with open(f'./listas/entrada_{size}.txt', 'w') as file:
        for item in entry:
            file.write(f"{item}\n")
    
    return entry

#====MÉTODOS============================================================================

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento a ser comparado
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insere o elemento na posição correta

# Ordenação de raiz usando Insertion Sort
def sqrt_insertion_sort(arr):
    n = len(arr)
    block_size = int(math.sqrt(n))  # Tamanho de cada seção
    blocks = [arr[i:i+block_size] for i in range(0, n, block_size)]
    
    # Ordena cada seção usando Insertion Sort
    for section in blocks:
        insertion_sort(section)
    
    sorted_arr = []
    while blocks:
        # Encontra a maior cabeça de seção
        max_block = max(blocks, key=lambda x: x[-1])
        sorted_arr.insert(0, max_block.pop())  # Adiciona ao início da lista ordenada
        if not max_block:
            blocks.remove(max_block)  # Remove seção vazia

    return sorted_arr

# Ordenação de raiz usando Heap
def sqrt_heap_sort(arr):
    n = len(arr)
    block_size = int(math.sqrt(n))  # Tamanho do bloco
    
    # Dividindo a lista em blocos
    blocks = [arr[i:i+block_size] for i in range(0, n, block_size)]
    
    # Construindo heaps máximos de cada bloco
    block_heaps = []
    for block in blocks:
        heapq._heapify_max(block)  # Construtor para heaps máximos
        block_heaps.append(block)
    
    # Construção da heap auxiliar
    max_heap = []
    for i in range(len(block_heaps)):
        if block_heaps[i]:
            heapq.heappush(max_heap, (-block_heaps[i][0], i))  # Usa - para simular heap máximo
    
    # Ordenando os elementos
    sorted_arr = []
    while max_heap:
        max_value, block_index = heapq.heappop(max_heap)  # Remove o maior elemento
        sorted_arr.append(-max_value)  # Adiciona o valor original ao resultado
        if block_heaps[block_index]:
            # Remove o maior elemento do bloco
            heapq._heappop_max(block_heaps[block_index])
            # Se ainda há elementos no bloco, re-adiciona o maior elemento
            if block_heaps[block_index]:
                heapq.heappush(max_heap, (-block_heaps[block_index][0], block_index))
    
    return sorted_arr

#====MAIN===============================================================================

def main():
    sizes = [1000, 10000, 100000, 1000000, 10000000]  # Tamanhos das entradas
    time1 = []
    time2 = []

    # Cria diretório se não existir
    if not os.path.exists('./resultados'):
        os.makedirs('./resultados')

    with open('./resultados/tempos_execucao.txt', 'w') as result_file:
        for size in sizes:
            print(f"================ Entrada de tamanho {size} ================")
            
            entry = gerar_entrada(size)  # Gera a entrada

            # Insertion Sort ===============================
            print("SQRT - Insertion Sort:")
            start = time.time()
            sorted_arr1 = sqrt_insertion_sort(entry.copy())  # Ordena a entrada
            end = time.time()
            elapsed_time = round(end - start, 3)  # Arredonda o tempo para 3 casas decimais
            time1.append(elapsed_time)  # Armazena o tempo
            result_file.write(f'{size} | Tempo Insertion Sort: {time1[-1]:.3f}s\n')
            print(f'Tempo de Ordenação: {time1[-1]:.3f}s\n')

            # Heap ==================================
            print("SQRT - Heap:")
            start = time.time()
            sorted_arr2 = sqrt_heap_sort(entry.copy())  # Ordena a entrada
            end = time.time()
            elapsed_time = round(end - start, 3)  # Arredonda o tempo para 3 casas decimais
            time2.append(elapsed_time)  # Armazena o tempo
            result_file.write(f'{size} | Tempo Heap: {time2[-1]:.3f}s\n')
            print(f'Tempo de Ordenação: {time2[-1]:.3f}s\n')

        result_file.write('\n')

        # Salvando os tempos de execução em formato de lista
        result_file.write(f'Insertion Sort: {time1}\n')
        result_file.write(f'Heap: {time2}\n')

    print("Insertion Sort:", time1)
    print("Heap:", time2)

if __name__ == "__main__":
    main()