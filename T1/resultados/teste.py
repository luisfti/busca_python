import matplotlib.pyplot as plt

def plot_values(time):
    
    entries = [10000, 100000, 1000000, 10000000]
    
    for i in range(len(time)):
        plt.figure(figsize=(10, 6))
        plt.plot(entries, time[i], marker='o', color='skyblue', linestyle='-')
        plt.xscale('log')  # Escala logarítmica para melhor visualização
        plt.xlabel('Número de Entradas')
        plt.ylabel('Tempo (s)',i)
        plt.title('Tempo de Execução em Relação ao Número de Entradas')
        plt.grid(True, which="both", ls="--", lw=0.5)
        plt.show()



time1 = [0.096, 3.815, 219.597, 0.098]
time2 = [0.095, 3.520, 205.636, 0.094]

time = [time1,time2]
plot_values(time)