import os


nome = input("Digite o nome da pasta: ")


pasta_inicial = "C:\\Users"


encontrou = False
contador = 0


for caminho, pastas, arquivos in os.walk(pasta_inicial):

    
    for pasta in pastas:

        
        if pasta.lower() == nome.lower():

            contador += 1
            encontrou = True

            print(f"\nResultado {contador}:")
            print(os.path.join(caminho, pasta))
            print("-" * 40)


if encontrou:
    print(f"\nForam encontradas {contador} pasta(s).")
else:
    print("\nPasta não encontrada.")