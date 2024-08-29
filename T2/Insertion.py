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