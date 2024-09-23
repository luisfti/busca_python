# Abordagem por programação dinâmica
def mochila_programacao_dinamica(itens, capacidade):
    n = len(itens)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if itens[i - 1].peso <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - itens[i - 1].peso] + itens[i - 1].valor)
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacidade]