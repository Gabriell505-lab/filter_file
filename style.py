import tkinter as tk
from tkinter import filedialog
import os

# -------------------------------

# -------------------------------
pasta_inicial = ""

# -------------------------------

# -------------------------------
def escolher_pasta():
    global pasta_inicial

    pasta_inicial = filedialog.askdirectory()

    print(f"Pasta escolhida: {pasta_inicial}")

# -------------------------------

# -------------------------------
def buscar():

    nome = entrada.get()

    
    lista_resultados.delete(0, tk.END)

    if pasta_inicial == "":
        lista_resultados.insert(
            tk.END,
            "Escolha uma pasta primeiro!"
        )
        return

    encontrou = False
    contador = 0

    for caminho, pastas, arquivos in os.walk(pasta_inicial):

        for pasta in pastas:

            if pasta.lower() == nome.lower():

                contador += 1
                encontrou = True

                lista_resultados.insert(
                    tk.END,
                    f"Resultado {contador}:"
                )

                lista_resultados.insert(
                    tk.END,
                    os.path.join(caminho, pasta)
                )

                lista_resultados.insert(
                    tk.END,
                    "-" * 60
                )

    if not encontrou:
        lista_resultados.insert(
            tk.END,
            "Pasta não encontrada."
        )

# -------------------------------

# -------------------------------
janela = tk.Tk()

janela.title("Buscador de Pastas")
janela.geometry("700x500")

# -------------------------------

# -------------------------------
titulo = tk.Label(
    janela,
    text="Buscador de Pastas",
    font=("Arial", 16)
)
titulo.pack(pady=10)

# -------------------------------

# -------------------------------
texto = tk.Label(
    janela,
    text="Digite o nome da pasta:"
)
texto.pack()

# -------------------------------

# -------------------------------
entrada = tk.Entry(
    janela,
    width=40
)
entrada.pack(pady=5)

# -------------------------------

# -------------------------------
botao_buscar = tk.Button(
    janela,
    text="Buscar",
    command=buscar
)
botao_buscar.pack(pady=5)

# -------------------------------

# -------------------------------
botao_pasta = tk.Button(
    janela,
    text="Escolher Pasta",
    command=escolher_pasta
)
botao_pasta.pack(pady=5)

# -------------------------------

# -------------------------------
lista_resultados = tk.Listbox(
    janela,
    width=90,
    height=15
)
lista_resultados.pack(pady=10)

# -------------------------------

# -------------------------------
janela.mainloop()