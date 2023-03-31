import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_posicoes =["Goleiro","Zagueiro", "Lateral", "Meio campo", "Atacante"]
lista_codigos =[]

janela = tk.Tk()

# Função
def inserir_codigo():
    nome = entry_nome.get()
    posicao = combobox_selecionar_posicao.get()
    idade = entry_idade.get()
    data_cadastro = dt.datetime.now()
    data_cadastro = data_cadastro.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos)+1
    codigo_str = "BID-{}".format(codigo)
    lista_codigos.append((codigo_str, nome, posicao, idade, data_cadastro))

# Janela

janela.title('Cadastro de Jogadores BID')
label_nome = tk.Label(text='Nome do jogador')
label_nome.grid(row=1, column=0, padx=15, pady=15, sticky='nswe', columnspan=4)

entry_nome = tk.Entry()
entry_nome.grid(row=2, column=0, padx=15, pady=15, sticky='nswe',columnspan=4)

label_tipo_posicao = tk.Label(text="Posição do jogador")
label_tipo_posicao.grid(row=3, column=0, padx=15, pady=15, sticky='nswe', columnspan=2)

combobox_selecionar_posicao = ttk.Combobox(values=lista_posicoes)
combobox_selecionar_posicao.grid(row=3, column=2, padx=15, pady=15, sticky='nswe', columnspan=2)

label_idade = tk.Label(text="Idade do jogador")
label_idade.grid(row=4, column=0, padx=15, pady=15, sticky='nswe', columnspan=2)

entry_idade = tk.Entry()
entry_idade.grid(row=4, column=2, padx=15, pady=15, sticky='nswe', columnspan=2)

botao_criar_codigo = tk.Button(text="Gerar código", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=15, pady=15, sticky='nswe', columnspan=4)


janela.mainloop()

print(lista_codigos)

