# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento a ser comparado
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insere o elemento na posição correta