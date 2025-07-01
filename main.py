from config.connection_redis import connection_redis
from config.connection_mongo import connection_mongo
from Menu.favorites import manager_favorites
from Menu.purchases import manager_purchases
from service.auth import login, user_logged

def main():
    db_mongo  = connection_mongo()
    db_redis = connection_redis()

    if db_mongo is None or db_redis is None:
        print('Erro ao conectar ao banco de dados.')
        return 

    mercado_livre_db = db_mongo['MercadoLivre']  
    product_col = mercado_livre_db['productCol']
    user_col = mercado_livre_db['userCol']
    purchases_col = mercado_livre_db['purchasesCol']

    user_email = input('Digite seu e-mail: ')
    user_password = input('Digite sua senha: ')

    user = login(user_col, db_redis,user_email, user_password)

    if user is None:
        return

    print("Bem-vindo ao Banco de Dados Do Mercado Livre")

    while True:

        if not user_logged(db_redis, user_email):
            print("Sessão expirada. Por favor, faça login novamente.")
            return

        print("-="*20)
        print("         Menu Principal")
        print("-="*20)
        print("1 - Favoritos")
        print("2 - Compras")
        print("0 - Sair")
        print("-="*20)

        try:
            choice = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida! Escolha novamente.")
            continue
        
        if choice == 1:
            manager_favorites(product_col, db_redis, user,user_col)
        elif choice == 2:
            manager_purchases(product_col, purchases_col, db_redis, user, user_col)
        elif choice == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Escolha novamente.")


if __name__ == "__main__":
    main()
        

