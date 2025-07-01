from service.purchase.create import create_purchase_form
from service.purchase.read import read_purchase

def manager_purchase(session):
    while True:
        print("_"*50)
        print(" "*50)
        print("     Menu de Compras")
        print("_"*50)
        print(" "*50)
        print("1. Criar Compra")
        print("2. Visualizar Compras")
        print("0. Voltar")
        
        choice = input("Escolha uma opção: ").strip()
        
        if choice == '1':
            create_purchase_form(session)  
        elif choice == '2':
            read_purchase(session)  
        elif choice == '0':
            print("Voltando ao menu anterior...")
            break  
        else:
            print("Opção inválida! Tente novamente.")