# Função de abordagem gulosa por menor peso
def mochila_gulosa_por_peso(itens, capacidade):
    itens_ordenados = sorted(itens, key=lambda x: x.peso)
    peso_atual, valor_total = 0, 0
    for item in itens_ordenados:
        if peso_atual + item.peso <= capacidade:
            peso_atual += item.peso
            valor_total += item.valor
    return valor_total