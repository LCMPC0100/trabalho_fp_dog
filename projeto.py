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

    print("     Cadastro de Animal")

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

    print("animal registrado com sucesso!\n")



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



def editar_animais():
    os.system("cls" if os.name == "nt" else "clear")
    print("     Editar Animal ")
    visualizar_animais()

    while True:
        try:
            indice=int(input("Insira o indice que queira editar: "))
            break
        
        except ValueError:
            print("Apenas numeros!\n")
    
    with open("animais.txt", "r", encoding="utf-8") as arquivo:
        animais=arquivo.readlines()
    
    if 0 <= indice < len(animais):
        dados = animais[indice].strip().split(",")
        
        print("\n deixe em branco para manter o valor atual.")

        nome = input(f"Nome ({dados[0]}): ")
        especie = input(f"Espécie ({dados[1]}): ")
        raca = input(f"Raça ({dados[2]}): ")
        idade = input(f"Idade ({dados[3]}): ")
        saude = input(f"Estado de saúde ({dados[4]}): ")
        chegada = input(f"Data de Chegada (DD-MM-AAAA)({dados[5]}): ")
        comportamento = input(f"Comportamento ({dados[6]}): ")

        animais[indice] = f"{nome},{especie},{raca},{idade},{saude},{chegada},{comportamento}\n"

        with open("animais.txt", "w", encoding="utf-8") as arquivo:
            arquivo.writelines(animais)

        print("Animal editado!")
    else:
        print("Indice invalido.")



def excluir_animais():
    os.system("cls" if os.name == "nt" else "clear")
    visualizar_animais()

    try:
        indice = int(input("\n Qual animal deseja excluir ? "))
    except ValueError:
        print("Apenas numeros !")
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
            print("Indice invalido.")

    except FileNotFoundError:
        print("Arquivo não encontrado.\n")



def adicionar_cuidados():
    
    os.system("cls" if os.name == "nt" else "clear")
    print("adicionar Cuidados")

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
        print("Apenas numeros!")
        return

    if not (0 <= indice < len(animais)):
        print("Índice invalido !")
        return

    cuidado = input("Descreva o cuidado: ")

    with open("cuidados.txt", "a", encoding="utf-8") as arq:
        arq.write(f"{indice},{cuidado}\n")

    print("Cuidado registrado com sucesso!\n")



def cadastro_tarefas():
    
    os.system("cls" if os.name == "nt" else "clear")
    print("Cadastro de Tarefas ")

    titulo = input("Titulo da tarefa: ")
    
    descricao = input("Descriçao: ")
    
    responsavel = input("Responsavel: ")
    
    data = input("Data (DD-MM-AAAA): ")

    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{titulo},{descricao},{responsavel},{data}\n")

    print("Tarefa registrada!\n")



def imprimir_gato():
    # Esqueci de fazer esse negocio e agora sao quase 3 da manha ;-;
    
    os.system("cls" if os.name == "nt" else "clear")

    gato = r"""
                                 #######         
                               ###     ####      
                             ###          ##     
                           ##      #       ##    
             #####   ######         #      ##    
             # #  ####   ########    #     ##    
             #  ##  #          ##### #     ##    
            ##   ## ##             ####     #    
            ##    ##  #####          ##     #    
             ##  ##        ##         #      #   
              ##             ###       #     #   
           ####                #####   ##    ##  
           ###     #####      #######   ##   ##  
    ##     ##    ## #####    # ### ####  ##  #   
    #####  ###   ## ###  #   # ### ## ########   
    #   ##   ##    #####      #####     #### ### 
    #     #   ##         ####          # #     ##
   ##     ##   ##     #   ##   #     ##  #     ##
   ##      #     ####  ########   ####    ## ### 
    #      #        ###         ###        ####  
     #     ##         ##########                 
      ##     ### #####  #   #  ##                
       ###     ###       ###    #                
         ######                 ##               
              ##             # ##                
              #      ###    # ##                 
              ##     ###   ## #                  
               ##    # ##  ### #                 
                #     ##    # ###                
                #### ##### #####                 
                   ###   ###                     


███████╗███████╗██╗     ██╗███████╗    ███╗   ██╗ █████╗ ████████╗ █████╗ ██╗     
██╔════╝██╔════╝██║     ██║██╔════╝    ████╗  ██║██╔══██╗╚══██╔══╝██╔══██╗██║     
█████╗  █████╗  ██║     ██║█████╗      ██╔██╗ ██║███████║   ██║   ███████║██║     
██╔══╝  ██╔══╝  ██║     ██║██╔══╝      ██║╚██╗██║██╔══██║   ██║   ██╔══██║██║     
██║     ███████╗███████╗██║███████╗    ██║ ╚████║██║  ██║   ██║   ██║  ██║███████╗
╚═╝     ╚══════╝╚══════╝╚═╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
    """

    print(gato)




def menu():
    
    
    while True:
        
        print(" Gerenciamento de Animais")
        
        print("[0] - Sair")
        
        print("[1] - Adicionar Animais")
        
        print("[2] - Visualizar Animais")
        
        print("[3] - excluir Animais")
        
        print("[5] - Adicionar Cuidados")
        
        print("[6] - Cadastro de Tarefas")
        
        print("[7] - Editar Animais")
        
        print("[8] -  Mostrar Gato Natalino")   
        
        try:
            opcao = int(input("\n -> "))
            
        except ValueError:
            print("Apenas numeros!\n")
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
        elif opcao == 7:
            editar_animais()
        elif opcao == 8:
            imprimir_gato()
        else:
            print("Opçao invlaida!\n")


menu()

