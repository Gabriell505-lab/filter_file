import os


nome = input("Digite o nome da pasta: ")


pasta_inicial = "C:\\Users"


encontrou = False

for caminho, pastas, arquivos in os.walk(pasta_inicial):

    
    for pasta in pastas:
        if pasta.lower() == nome.lower():
            print("Pasta encontrada!")
            print(os.path.join(caminho, pasta))
            print("-" * 40)
            encontrou = True


if not encontrou:
    print("Pasta não encontrada.")