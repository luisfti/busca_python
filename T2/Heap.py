def sqrt_heap_sort(arr):
    n = len(arr)
    block_size = int(math.sqrt(n))
    blocks = [arr[i:i+block_size] for i in range(0, n, block_size)]
    
    block_heaps = []
    for block in blocks:
        heapq._heapify_max(block)
        block_heaps.append(block)
    
    max_heap = []
    for i in range(len(block_heaps)):
        if block_heaps[i]:
            heapq.heappush(max_heap, (-block_heaps[i][0], i))
    
    sorted_arr = []
    while max_heap:
        max_value, block_index = heapq.heappop(max_heap)
        sorted_arr.append(-max_value)
        if block_heaps[block_index]:
            heapq._heappop_max(block_heaps[block_index])
            if block_heaps[block_index]:
                heapq.heappush(max_heap, (-block_heaps[block_index][0], block_index))
    
    return sorted_arr
