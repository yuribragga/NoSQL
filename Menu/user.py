from service.user.create import create_user_form
from service.user.read import read_usuario

def manager_user(session):
    while True:
        print("_"*50)
        print(" "*50)
        print("         Menu Usuários")
        print("_"*50)
        print(" "*50)
        print("1. Criar Usuário")
        print("2. Visualizar Usuários")
        print("0. Sair")
        print("_"*50)
        print(" "*50)
        
        choice = input("Escolha uma opção: ").strip()
        
        match choice:
            case "1":
                create_user_form(session)
            case "2":
                read_usuario(session)
            case "0":
                print("Saindo do Gerenciador de Usuários.")
                break
            case _:
                print("Opção inválida. Tente novamente.")