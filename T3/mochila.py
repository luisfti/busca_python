import os
import matplotlib.pyplot as plt
import time
import numpy as np

# Classe Item
class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

# Função para ler os dados dos arquivos, organizar e processar
def ler_dados(diretorio):
    # Subpasta onde os arquivos estão localizados
    subpastas = ['knaPI_1', 'knaPI_2', 'knaPI_3']
    dados = {}

    # Itera sobre as subpastas especificadas
    for subpasta in subpastas:
        caminho_pasta = os.path.join(diretorio, subpasta)
        arquivos = os.listdir(caminho_pasta)  # Lista todos os arquivos na subpasta
        dados[subpasta] = {}

        # Lista que armazenará os dados dos arquivos para posterior ordenação
        arquivos_com_itens = []

        # Processa cada arquivo dentro da subpasta
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            
            with open(caminho_arquivo, 'r') as f:
                linhas = f.readlines()  # Lê todas as linhas do arquivo
                
                # Primeira linha contém a capacidade da mochila
                primeira_linha = linhas[0].split()
                capacidade = int(primeira_linha[1])
                
                itens = []  # Lista para armazenar os itens (peso e valor)
                otimo = []  # Lista para armazenar o vetor ótimo

                # Processa todas as linhas exceto a última (vetor ótimo)
                for linha in linhas[1:-1]:
                    linha = linha.strip()
                    if linha:  # Garante que a linha não está vazia
                        valor, peso = map(int, linha.split())  # Extrai valor e peso
                        itens.append(Item(peso, valor))  # Adiciona o item à lista

                # Processa a última linha que contém o vetor ótimo
                otimo = list(map(int, linhas[-1].strip().split()))
                
                # Armazena os dados do arquivo na lista, para ordenar posteriormente
                arquivos_com_itens.append((arquivo, capacidade, itens, otimo))

        # Ordena a lista de arquivos com base na quantidade de itens (do menor para o maior)
        arquivos_com_itens.sort(key=lambda x: len(x[2]))  # x[2] é a lista de itens

        # Após a ordenação, insere os dados no dicionário final
        for arquivo, capacidade, itens, otimo in arquivos_com_itens:
            dados[subpasta][arquivo] = {'capacidade': capacidade, 'itens': itens, 'otimo': otimo}


    return dados

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

# Função principal de geração de gráficos
def gerar_graficos(diretorio):
    # Cria o diretório para os resultados, se não existir
    resultados_dir = 'resultados'
    if not os.path.exists(resultados_dir):
        os.makedirs(resultados_dir)
    
    # Abre o arquivo de texto para salvar os resultados dos prints de debug
    debug_file_path = os.path.join(resultados_dir, 'debug.txt')
    with open(debug_file_path, 'w') as debug_file:

        dados = ler_dados(diretorio)
        xs = [100, 200, 500, 1000, 2000, 5000, 10000]  # Valores de x
        time1 = []
        time2 = []
        time3 = []
        qualidade1 = []
        qualidade2 = []
        qualidade3 = []
        
        # Pasta para salvar os gráficos
        graficos_dir = 'graficos'
        if not os.path.exists(graficos_dir):
            os.makedirs(graficos_dir)

        for tipo_instancia, instancia_dados in dados.items():

            # Zera as listas ao final da geração do gráfico
            time1.clear()
            time2.clear()
            time3.clear()
            qualidade1.clear()
            qualidade2.clear()
            qualidade3.clear()

            for arquivo, conteudo in instancia_dados.items():
                capacidade = conteudo['capacidade']
                itens = conteudo['itens']
                otimo = conteudo['otimo']

                # Validação para garantir que o tamanho do vetor 'otimo' corresponde ao número de itens
                
                print(f"{arquivo} {len(itens)} {len(otimo)}")
                
                
                valor_otimo = sum([itens[i].valor for i in range(len(itens)) if otimo[i] == 1])

                # Execução gulosa por peso
                start = time.time()
                resultado_gulosa_peso = mochila_gulosa_por_peso(itens, capacidade)
                end = time.time()
                elapsed_time = end - start
                time1.append(round(elapsed_time, 3) if elapsed_time > 0 else 1e-6)  # Substitui 0 por 1e-6
                qualidade1.append(round(resultado_gulosa_peso / valor_otimo, 3))
                
                # Salva a linha no arquivo de debug
                debug_file.write(f"Arquivo: {arquivo} - Valor Ótimo: {valor_otimo}, Resultado Gulosa por Peso: {resultado_gulosa_peso}\n")

                # Execução gulosa por benefício/custo
                start = time.time()
                resultado_gulosa_beneficio = mochila_gulosa_por_beneficio_custo(itens, capacidade)
                end = time.time()
                elapsed_time = end - start
                time2.append(round(elapsed_time, 3) if elapsed_time > 0 else 1e-6)  # Substitui 0 por 1e-6
                qualidade2.append(round(resultado_gulosa_beneficio / valor_otimo, 3))
               
                
                # Salva a linha no arquivo de debug
                debug_file.write(f"Arquivo: {arquivo} - Valor Ótimo: {valor_otimo}, Resultado Gulosa por Benefício/Custo: {resultado_gulosa_beneficio}\n")

                # Execução por programação dinâmica
                start = time.time()
                resultado_dinamica = mochila_programacao_dinamica(itens, capacidade)
                end = time.time()
                elapsed_time = end - start
                time3.append(round(elapsed_time, 3) if elapsed_time > 0 else 1e-6)  # Substitui 0 por 1e-6
                qualidade3.append(round(resultado_dinamica / valor_otimo, 3))
                print(f" valor: {resultado_dinamica}  - {valor_otimo}")
                
                # Salva a linha no arquivo de debug
                debug_file.write(f"Arquivo: {arquivo} - Valor Ótimo: {valor_otimo}, Resultado Programação Dinâmica: {resultado_dinamica}\n")
                
                debug_file.write("\n")

            # Salva os tempos e qualidades no arquivo de debug
            debug_file.write(f"\nTipo de Instância: {tipo_instancia}\n")
            debug_file.write(f"Tempo de Execução - Peso: {time1}\n")
            debug_file.write(f"Tempo de Execução - Benefício: {time2}\n")
            debug_file.write(f"Tempo de Execução - Dinâmica: {time3}\n")
            debug_file.write(f"Qualidade - Peso: {qualidade1}\n")
            debug_file.write(f"Qualidade - Benefício: {qualidade2}\n")
            debug_file.write(f"Qualidade - Dinâmica: {qualidade3}\n")

            debug_file.write("\n")

            # Gráfico de curvas para o tempo de execução
            plt.plot(xs, time1, label='Gulosa - Menor Peso', marker='o')
            plt.plot(xs, time2, label='Gulosa - Benefício/Custo', marker='o')
            plt.plot(xs, time3, label='Programação Dinâmica', marker='o')
            plt.xscale('log')
            plt.yscale('log')
            plt.title(f'Tempo de Execução ({tipo_instancia}) vs Número de Itens')
            plt.xlabel('Número de Itens (x)')
            plt.ylabel('Tempo de Execução (s)')
            plt.legend()
            plt.grid(True)
            
            # Salva o gráfico na pasta 'graficos'
            grafico_tempo_path = os.path.join(graficos_dir, f'tempo_execucao_{tipo_instancia}.png')
            plt.savefig(grafico_tempo_path)
            plt.clf()

            # Gráfico de barras para a qualidade da solução
            plt.figure(figsize=(10, 5))
            width = 0.2
            x = np.arange(len(xs))

            plt.bar(x - width, qualidade1, width=width, label='Gulosa - Menor Peso')
            plt.bar(x, qualidade2, width=width, label='Gulosa - Benefício/Custo')
            plt.bar(x + width, qualidade3, width=width, label='Programação Dinâmica')
            
            plt.xticks(x, xs)  # Ajusta os ticks do eixo x para corresponder a xs
            plt.title(f'Qualidade da Solução ({tipo_instancia}) vs Número de Itens')
            plt.xlabel('Número de Itens (x)')
            plt.ylabel('Qualidade da Solução (q)')
            
            plt.legend()
            plt.grid(True)

            # Salva o gráfico na pasta 'graficos'
            grafico_qualidade_path = os.path.join(graficos_dir, f'qualidade_solucao_{tipo_instancia}.png')
            plt.savefig(grafico_qualidade_path)
            plt.clf()

            

# Exemplo de como utilizar a função:
gerar_graficos('./teste')