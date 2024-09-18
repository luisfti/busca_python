import os
import matplotlib.pyplot as plt
import time
import numpy as np

# Classe Item
class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor


# Função para ler os dados dos três diretórios de arquivos
def ler_dados(diretorio):
    subpastas = ['knaPI_1', 'knaPI_2', 'knaPI_3']
    dados = {}
    
    for subpasta in subpastas:
        caminho_pasta = os.path.join(diretorio, subpasta)
        arquivos = os.listdir(caminho_pasta)
        dados[subpasta] = {}
        
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            with open(caminho_arquivo, 'r') as f:
                primeira_linha = f.readline().split()
                capacidade = int(primeira_linha[1])
               
                itens = []
                otimo = []  # Inicializar o vetor ótimo como vazio
                for linha in f:
                    linha = linha.strip()  # Remove espaços em branco no início e no final
            
                    if not linha:  # Ignora linhas vazias
                        continue
                    if all(c in "01" for c in linha.replace(" ", "")):  # Verifica se a linha contém apenas '0' e '1'
                        otimo = list(map(int, linha.split()))  # Converte a linha em lista de inteiros
                    else:
                        try:
                            valor, peso = map(int, linha.split())
                            itens.append(Item(peso, valor))
                        except ValueError:
                            print(f"Erro ao processar linha: {linha}")
                            continue
                
                        
            dados[subpasta][arquivo] = {'capacidade': capacidade, 'itens': itens, 'otimo': otimo}
            #print(f"Dados do arquivo '{arquivo}': Capacidade: {capacidade}, Quantidade de Itens: {len(itens)}, Tamanho do Vetor Ótimo: {len(otimo)}")
    
    return 

# Função de abordagem gulosa por menor peso
def mochila_gulosa_por_peso(itens, capacidade):
    itens_ordenados = sorted(itens, key=lambda x: x.peso)
    peso_atual, valor_total = 0, 0
    for item in itens_ordenados:
        if peso_atual + item.peso <= capacidade:
            peso_atual += item.peso
            valor_total += item.valor
    return valor_total

# Função de abordagem gulosa por melhor benefício/custo
def mochila_gulosa_por_beneficio_custo(itens, capacidade):
    itens_ordenados = sorted(itens, key=lambda x: x.valor / x.peso, reverse=True)
    peso_atual, valor_total = 0, 0
    for item in itens_ordenados:
        if peso_atual + item.peso <= capacidade:
            peso_atual += item.peso
            valor_total += item.valor
    return valor_total

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

# Função para gerar gráficos
def gerar_graficos(diretorio):
    dados = ler_dados(diretorio)
    xs = [100, 200, 500, 1000, 2000, 5000, 10000]  # Valores de y
    time1 = []
    time2 = []
    time3 = []
    qualidade1 = []
    qualidade2 = []
    qualidade3 = []

    for tipo_instancia, instancia_dados in dados.items():
        tempo_execucao = {'peso': [], 'beneficio': [], 'dinamica': []}
        qualidade = {'peso': [], 'beneficio': [], 'dinamica': []}

        for arquivo, conteudo in instancia_dados.items():
            capacidade = conteudo['capacidade']
            itens = conteudo['itens']
            otimo = conteudo['otimo']
            
            if len(itens) not in xs:
                continue  # Ignora instâncias cujo número de itens não está em ys

            # Execução gulosa por peso
            start = time.time()
            resultado_gulosa_peso = mochila_gulosa_por_peso(itens, capacidade)
            end = time.time()
            elapsed_time = round(end - start, 3)  # Arredonda o tempo para 3 casas decimais
            time1.append(elapsed_time)  # Armazena o tempo
            valor_otimo = sum([itens[i].valor for i in range(len(itens)) if otimo[i] == 1])
            print(f"Arquivo: {arquivo} - Valor Ótimo: {valor_otimo}, Resultado Gulosa por Peso: {resultado_gulosa_peso}")  # Debugging
            if valor_otimo > 0:
                qualidade1.append(round(resultado_gulosa_peso / valor_otimo, 3))
            else:
                qualidade1.append(0)

            # Execução gulosa por benefício/custo
            start = time.time()
            resultado_gulosa_beneficio = mochila_gulosa_por_beneficio_custo(itens, capacidade)
            end = time.time()
            elapsed_time = round(end - start, 3)  # Arredonda o tempo para 3 casas decimais
            time2.append(elapsed_time)  # Armazena o tempo
            if valor_otimo > 0:
                qualidade2.append(round(resultado_gulosa_beneficio / valor_otimo, 3))
            else:
                qualidade2.append(0)

            # Execução por programação dinâmica
            start = time.time()
            resultado_dinamica = mochila_programacao_dinamica(itens, capacidade)
            end = time.time()
            elapsed_time = round(end - start, 3)  # Arredonda o tempo para 3 casas decimais
            time3.append(elapsed_time)  # Armazena o tempo
            if valor_otimo > 0:
                qualidade3.append(round(resultado_dinamica / valor_otimo, 3))
            else:
                qualidade3.append(0)


        
        # Debugging prints
        print(f"\nTipo de Instância: {tipo_instancia}")
        print(f"Xs: {xs}")
        print(f"Tempo de Execução - Peso: {time1}")
        print(f"Tempo de Execução - Benefício: {time2}")
        print(f"Tempo de Execução - Dinâmica: {time3}")
        print(f"Qualidade - Peso: {qualidade1}")
        print(f"Qualidade - Benefício: {qualidade2}")
        print(f"Qualidade - Dinâmica: {qualidade3}")

        # Gráfico de curvas para o tempo de execução
        plt.figure(figsize=(10, 5))
        plt.plot(xs, time1, label='Gulosa - Menor Peso', marker='o')
        plt.plot(xs, time2, label='Gulosa - Benefício/Custo', marker='o')
        plt.plot(xs, time3, label='Programação Dinâmica', marker='o')
        plt.xscale('log')  # Escala logarítmica para o eixo X
        plt.yscale('log')  # Escala logarítmica para o eixo Y
        plt.title(f'Tempo de Execução ({tipo_instancia}) vs Número de Itens')
        plt.xlabel('Número de Itens (x)')
        plt.ylabel('Tempo de Execução (s)')
        plt.legend()
        plt.grid(True)
        plt.show()

        # Gráfico de barras para a qualidade da solução
        plt.figure(figsize=(10, 5))
        width = 0.2
        x = np.arange(len(xs))

        plt.bar(x - width, qualidade1, width=width, label='Gulosa - Menor Peso')
        plt.bar(x, qualidade2, width=width, label='Gulosa - Benefício/Custo')
        plt.bar(x + width, qualidade3, width=width, label='Programação Dinâmica')

        plt.title(f'Qualidade da Solução ({tipo_instancia}) vs Número de Itens')
        plt.xlabel('Número de Itens (y)')
        plt.ylabel('Qualidade da Solução (q)')
        
        plt.legend()
        plt.grid(True)
        plt.show()

# Exemplo de uso:
gerar_graficos('./teste')