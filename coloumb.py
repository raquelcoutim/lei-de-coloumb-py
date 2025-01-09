import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import customtkinter
import numpy as np

valorCarga1 = []
valorCarga2 = []
distanciaCarga = []
valorCalculo = ["Ainda não há nada aqui."]


def func_calculo():
    valorCarga1.insert(0, eval(carga1Value.get()))
    valorCarga2.insert(0, eval(carga2Value.get()))
    distanciaCarga.insert(0, eval(distanciaValue.get()))
    if valorCarga1[0] > 0:
        valorCarga1.insert(1, "positiva")
    elif valorCarga1[0] < 0:
        valorCarga1.insert(1, "negativa")
    if valorCarga2[0] > 0:
        valorCarga2.insert(1, "positiva")
    elif valorCarga2[0] < 0: 
        valorCarga2.insert(1, "negativa")
    valorCalculo.insert(0, (((9 * 10 ** 9) * abs(valorCarga1[0]) * abs(valorCarga2[0]))/distanciaCarga[0] ** 2))
    forcaEletrostatica.configure(text="O resultado é: {}.".format(np.format_float_scientific(np.float32(valorCalculo[0]))))

    x = [0, distanciaCarga[0]]
    y = [distanciaCarga[0] * 2, distanciaCarga[0] * 2]
    z = [distanciaCarga[0] * 2, distanciaCarga[0] *2]

    if abs(valorCarga1[0]) > abs(valorCarga2[0]):
        sizes = [50, 50 * (valorCarga1[0]/valorCarga2[0])]
    elif abs(valorCarga1[0]) < abs(valorCarga2[0]):
        sizes = [50, 50 * (valorCarga2[0]/valorCarga1[0])]
    elif abs(valorCarga1[0]) == abs(valorCarga2[0]):
        sizes = [50, 50]

    distancia = np.sqrt((x[1] - x[0])**2 + (y[1] - y[0])**2 + (z[1] - z[0])**2)

    dx = x[1] - x[0]
    dy = y[1] - y[0]
    dz = z[1] - z[0]

    fig = plt.figure(figsize=(13, 10))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot([x[0], x[1]], [y[0], y[1]], [z[0], z[1]], color='r', label=f'Distância = {distancia}')

    if valorCarga1[1] == valorCarga2[1]:
        ax.quiver(x[1], y[1], z[1], dx/4, dy/4, dz/4, color='g', arrow_length_ratio=0.1, linewidth=1.5)  
        ax.quiver(x[0], y[0], z[0], -dx/4, -dy/4, -dz/4, color='g', arrow_length_ratio=0.1, linewidth=1.5) 

    elif valorCarga1[1] != valorCarga2[1]:
        ax.quiver(x[1], y[1], z[1], -dx/4, -dy/4, -dz/4, color='g', arrow_length_ratio=0.1, linewidth=1.5)
        ax.quiver(x[0], y[0], z[0], dx/4, dy/4, dz/4, color='g', arrow_length_ratio=0.1, linewidth=1.5) 
        
    ax.scatter(x, y, z, s=sizes)
    plt.show()


janela = customtkinter.CTk()
janela.title("Lei de Coloumb - Eletrostática")
janela.geometry("600x380")

carga1 = customtkinter.CTkLabel(janela, text="Digite o valor da primeira carga (em coloumbs)", font=("Arial", 14, "bold"))
carga1.pack(pady=15)
carga1Value = customtkinter.CTkEntry(janela)
carga1Value.pack()

carga2 = customtkinter.CTkLabel(janela, text="Digite o valor da segunda carga (em coloumbs)", font=("Arial", 14, "bold"))
carga2.pack(pady=15)
carga2Value = customtkinter.CTkEntry(janela)
carga2Value.pack()

distancia = customtkinter.CTkLabel(janela, text="Digite o valor da distância (em metros)", font=("Arial", 14, "bold"))
distancia.pack(pady=15)
distanciaValue = customtkinter.CTkEntry(janela)
distanciaValue.pack()

button = customtkinter.CTkButton(janela, text="Calcular", command=func_calculo)
button.pack(pady=15)
forcaEletrostatica = customtkinter.CTkLabel(janela, text="")
forcaEletrostatica.pack(pady=15)

janela.resizable(width=False, height=False)
janela.mainloop()

