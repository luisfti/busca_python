# Sequencial
def buscaSequencial(entry, key):
    for i in range(len(entry)):
        if entry[i] > key:
            return -1
        elif entry[i] == key:
            return i
    return -1