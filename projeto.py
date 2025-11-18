import os

def apenas_letras(pergunta):
    while True:
        
        texto = input(pergunta).strip()
        
        if texto.replace(" ", "").isalpha():  
            return texto
        
        else:
            print("digite apenas letras.\n")


def adicionar_animais():
    os.system("cls" if os.name == "nt" else "clear")

    print("    Cadastro de Animal    ")

    nome = apenas_letras("Nome: ")
    especie = apenas_letras("Espécie: ")
    raca = apenas_letras("Raça: ")

    
    while True:
        
        try:
            idade = int(input("Idade: "))
            break
        
        except ValueError:
            print("Apenas numeros!\n")

    saude = apenas_letras("Estado de saude: ")
    chegada = input("Data de Chegada (DD-MM-AAAA): ")  
    comportamento = apenas_letras("Comportamento: ")

    with open("animais.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{especie},{raca},{idade},{saude},{chegada},{comportamento}\n")

    print("Animal Registrado com sucesso!\n")



def visualizar_animais():
    os.system("cls" if os.name == "nt" else "clear")

    try:
        
        with open("animais.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("Nenhum animal registrado.\n")
            return

        for indice, linha in enumerate(linhas):
            dados = linha.strip().split(",")
            print(f"{indice} - Nome: {dados[0]} | Espécie: {dados[1]} | Raça: {dados[2]} | Idade: {dados[3]} | Saúde: {dados[4]} | Chegada: {dados[5]} | Comportamento: {dados[6]}")

    except FileNotFoundError:
        print("Arquivo de animais não encontrado.\n")



def excluir_animais():
    visualizar_animais()

    try:
        
        indice = int(input("\nQual animal deseja excluir? "))
        
    except ValueError:
        print("Apenas números!")
        return

    try:
        
        with open("animais.txt", "r", encoding="utf-8") as arquivo:
            animais = arquivo.readlines()

        if not animais:
            print("Nenhum animal registrado.\n")
            return

        if 0 <= indice < len(animais):
            del animais[indice]

            with open("animais.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(animais)

            print("Animal removido com sucesso!")
        else:
            print("Índice inválido.")

    except FileNotFoundError:
        print("Arquivo não encontrado.\n")



def adicionar_cuidados():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Adicionar Cuidados ===")

    try:
        
        with open("animais.txt", "r", encoding="utf-8") as arquivo:
            animais = arquivo.readlines()
            
    except FileNotFoundError:
        print("Nenhum animal encontrado.")
        return

    if not animais:
        print("Nenhum animal registrado.")
        return

   
    for i, linha in enumerate(animais):
        dados = linha.strip().split(",")
        print(f"{i} - {dados[0]} ({dados[1]})")

    try:
        indice = int(input("Selecione o animal: "))
        
    except ValueError:
        print("Apenas números!")
        return

    if not (0 <= indice < len(animais)):
        print("Índice inválido!")
        return

    cuidado = input("Descreva o cuidado: ")

    with open("cuidados.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{indice},{cuidado}\n")

    print("Cuidado registrado com sucesso!\n")



def cadastro_tarefas():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Cadastro de Tarefas ===")

    titulo = input("Titulo da tarefa: ")
    descricao = input("Descrição: ")
    responsavel = input("Responsável: ")
    data = input("Data (DD-MM-AAAA): ")

    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{titulo},{descricao},{responsavel},{data}\n")

    print("Tarefa registrada!\n")



def menu():
    
    while True:
        
        print("=== Gerenciamento de Animais ===")
        print("[0] - Sair")
        print("[1] - Adicionar Animais")
        print("[2] - Visualizar Animais")
        print("[3] - Excluir Animais")
        print("[5] - Adicionar Cuidados")
        print("[6] - Cadastro de Tarefas")
        print("[7] - editar")
        
        

        try:
            opcao = int(input("-> "))
            
        except ValueError:
            print("Apenas números!\n")
            continue

        if opcao == 0:
            break
        elif opcao == 1:
            adicionar_animais()
        elif opcao == 2:
            visualizar_animais()
        elif opcao == 3:
            excluir_animais()
        elif opcao == 5:
            adicionar_cuidados()
        elif opcao == 6:
            cadastro_tarefas()
        else:
            print("Opção inválida!\n")


menu()
