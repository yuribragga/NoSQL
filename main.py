from config.connection_neo4j import connection_neo4j
from menu.product import manager_product
from menu.purchase import manager_purchase
from menu.seller import manager_seller
from menu.user import manager_user

def main():
    driver, session = connection_neo4j()

    if driver is None or session is None:
        print("Erro ao conectar ao banco de dados.")
        return
    
    while True:
        print("_"*50)
        print(" "*50)
        print("        Mercado Livre - Neo4j")
        print("_"*50)
        print(" "*50)
        print("1. Gerenciar Usuario")
        print("2. Gerenciar Vendedor")
        print("3. Gerenciar Produto")
        print("4. Gerenciar Compras")
        print("0. Sair ")
        print(" "*50)
        print("_"*50)

        try:
            print(" "*50)
            choice = int(input("Digite a opção que deseja: "))
        except ValueError as e:
            print(f"[Error] : {e}")
            continue

    
        match choice:
            case 1:
                manager_user(session)
            case 2:
                manager_seller(session) 
            case 3:
                manager_product(session)  
            case 4:
                manager_purchase(session)  
            case 0:
                session.close()  
                driver.close()  
                print("Saindo...")
                break  
            case _:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()