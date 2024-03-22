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