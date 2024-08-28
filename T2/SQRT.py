# Ordenação de raiz usando Heap Sort
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
