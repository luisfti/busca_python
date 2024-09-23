# Função de abordagem gulosa por melhor benefício/custo
def mochila_gulosa_por_beneficio_custo(itens, capacidade):
    itens_ordenados = sorted(itens, key=lambda x: x.valor / x.peso, reverse=True)
    peso_atual, valor_total = 0, 0
    for item in itens_ordenados:
        if peso_atual + item.peso <= capacidade:
            peso_atual += item.peso
            valor_total += item.valor
    return valor_total