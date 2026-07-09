import tkinter as tk

# Criando a janela
janela = tk.Tk()

# Configurando a janela
janela.title("Buscador de Pastas")
janela.geometry("600x400")

# Texto
texto = tk.Label(janela, text="Digite o nome da pasta:")
texto.pack()

# Caixa de texto
entrada = tk.Entry(janela)
entrada.pack()

# Função que será executada quando clicar no botão
def buscar():
    nome = entrada.get()
    print(nome)

# Botão
botao = tk.Button(
    janela,
    text="Buscar",
    command=buscar
)
botao.pack()

# Mantém a janela aberta
janela.mainloop()