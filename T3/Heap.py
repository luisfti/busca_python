def knapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Construa a tabela K[][] em ordem ascendente
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    return K[n][W]


def maximize_items(W, wt, val, n):
    value = [0 for i in range(W+1)]
    for i in range(1, W+1):
        for j in range(n):
            if wt[j] <= i:
                value[i] = max(value[i], value[i - wt[j]] + val[j])
    return value[W]


def maximize_value(W, wt, val, n):
    K = [[0 for w in range(W+1)] for i in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

# Valores (val) e pesos (wt) dos itens
val = [60, 100, 120, 130, 150]
wt = [10, 20, 30, 40, 50]
# Capacidade da mochila
W = 50
n = len(val)
 
print(knapSack(W, wt, val, n))