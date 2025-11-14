import os

def adicionar_animais():
    os.system("cls" if os.name == "nt" else "clear")

    print("=== Cadastro de Animal ===")
    nome = input("Nome: ")
    especie = input("Especie: ")
    raca = input("Raça: ")

    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Apenas numeros")
    
    saude = input("Estado de saúde: ")
    chegada = input("Data de Chegada (AAAA-MM-DD): ")
    comportamento = input("Comportamento: ")

    with open("animais.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{especie},{raca},{str(idade)},{saude},{chegada},{comportamento}\n")
    print("Animal Registrado")

def visualizar_animais():
    os.system("cls" if os.name == "nt" else "clear")

    try:
        with open("animais.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("Nenhum animal registrado\n")
            else:
                for indice, linha in enumerate(linhas):
                    dados= linha.strip().split(",")
                    print(f"{indice} - Nomes: {dados[0]} | Espécie: {dados[1]} | Raça: {dados[2]} | Idade: {dados[3]} | Saúde {dados[4]} | Chegada: {dados[5]} | Comportamento: {dados[6]}")

    except FileNotFoundError:
        print("Arquivo não encontrado")

def excluir_animais():
    visualizar_animais()
    try:
        indice = int(input("Qual animal desejas excluir? ")) - 1
    except ValueError:
        print("Apenas números!")
    
    try:
        with open("animais.txt", "r", encoding="utf-8") as arquivo:
            animais = arquivo.readlines()
        
        if not animais:
            print("Nenhum animal registrado.")

        if 0 <= indice < len(animais):
            del animais[indice]

            with open("animais.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(animais)

            print("Animal removido!")
        else:
            print("Índice inválido.")

    except FileNotFoundError:
        print("Arquivo não encontrado.")    

def menu():
    while True:
        print("=== Gerenciamento de Animais ===")
        print("[0] - Sair \n[1] - Adicionar Animais \n[2] - Visualizar Animais \n[3] - Excluir Animais \n[5] - Adicionar Cuidados \n[6] - Cadastro de Tarefas")
        try:
            opcao=int(input("-> "))

            if opcao == 0:
                break
            elif opcao == 1:
                adicionar_animais()
            elif opcao == 2:
                visualizar_animais()
            elif opcao == 3:
                excluir_animais()
            else:
                print("Erro, numero não encontrado na tabela")
        except ValueError:
            print("Apenas numeros")

menu()