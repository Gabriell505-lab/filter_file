import os

# Pergunta o nome da pasta
nome = input("Digite o nome da pasta: ")

# Pasta onde a busca vai começar
pasta_inicial = "C:\\Users"

# Variável para saber se encontrou ou não
encontrou = False

# Percorre todas as pastas
for caminho, pastas, arquivos in os.walk(pasta_inicial):

    # Verifica se existe uma pasta com esse nome (ignorando maiúsculas/minúsculas)
    for pasta in pastas:
        if pasta.lower() == nome.lower():
            print("Pasta encontrada!")
            print(os.path.join(caminho, pasta))
            print("-" * 40)
            encontrou = True

# Se não encontrou nenhuma pasta
if not encontrou:
    print("Pasta não encontrada.")