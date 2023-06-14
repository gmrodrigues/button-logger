import tkinter as tk
import matplotlib.pyplot as plt
from datetime import datetime

# Dados iniciais
registros = {
    'iniciei_trabalho': [],
    'finalizei': [],
    'estou_cansado': [],
    'me_distrair': []
}

# Função para registrar o tempo atual
def registrar_botao(botao):
    tempo = datetime.now().strftime('%H:%M:%S')
    registros[botao].append(tempo)
    print(f'Botão {botao} pressionado às {tempo}')

# Função para exibir o gráfico
def exibir_grafico():
    plt.figure(figsize=(8, 6))
    for botao, tempos in registros.items():
        tempos_convertidos = [datetime.strptime(t, '%H:%M:%S') for t in tempos]
        plt.plot(tempos_convertidos, [botao] * len(tempos_convertidos), 'o', label=botao)
    plt.xlabel('Hora')
    plt.ylabel('Botão')
    plt.title('Registros dos botões')
    plt.legend()
    plt.show()

# Interface gráfica
root = tk.Tk()
root.title('Registro de Botões')

# Botões
btn_iniciar = tk.Button(root, text='Iniciei trabalho', command=lambda: registrar_botao('iniciei_trabalho'))
btn_iniciar.pack()

btn_finalizar = tk.Button(root, text='Finalizei', command=lambda: registrar_botao('finalizei'))
btn_finalizar.pack()

btn_cansado = tk.Button(root, text='Estou cansado', command=lambda: registrar_botao('estou_cansado'))
btn_cansado.pack()

btn_distrair = tk.Button(root, text='Me distrair', command=lambda: registrar_botao('me_distrair'))
btn_distrair.pack()

btn_grafico = tk.Button(root, text='Exibir gráfico', command=exibir_grafico)
btn_grafico.pack()

root.mainloop()
