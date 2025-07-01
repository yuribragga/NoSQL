from uuid import uuid4
from datetime import datetime
from utils.utils import list_products, get_product, update_sale_and_stock, get_user, row_to_dict_user

def create_purchase(db, user_id):
    try:
        purchase_id = str(uuid4())
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados da nova compra:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        user = get_user(db, user_id)
        if user is None:
            print("Usuário não encontrado!")
            return
        user_data = row_to_dict_user(user)
        
        products = list_products(db)
        if not products:
            print("Sem produtos cadastrados no sistema.")
            return
        
        produtos = []
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            product_id = input("Digite o ID do produto que deseja comprar: ")
            quantity = int(input("Digite a quantidade do produto: "))
            
            product = get_product(db, product_id)
            if product is None:
                print("Produto não encontrado!")
                continue  

            if quantity > product.get('estoque', 0):
                print(f"Quantidade disponível para venda: {product.get('estoque', 0)}")
                continue
            
            produtos.append({
                "produto_id": product_id,
                "nome_produto": product.get('nome_produto', ''),
                "quantidade": str(quantity),
                "preco_unitario": str(product.get('valor', 0.0))
            })

            continuar = input("Deseja adicionar outro produto? (s/n): ")
            if continuar.lower() != 's':
                break

        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Selecione um endereço de entrega:")
        
        enderecos = user_data.get("enderecos", [])
        if not enderecos:
            print("Você não tem endereços cadastrados!")
            return
        
        for idx, end in enumerate(enderecos, start=1):
            print(f"{idx} - {end['rua']}, {end['bairro']}, {end['cidade']}")

        try:
            index_to_select = int(input("Digite o número do endereço a ser selecionado (ou 0 para cancelar): "))
            if 0 < index_to_select <= len(enderecos):
                endereco_entrega = dict(enderecos[index_to_select - 1])
            else:
                print("Seleção inválida ou operação cancelada.")
                return
        except ValueError:
            print("Por favor, insira um número válido.")
            return
        
        valor_total = sum(float(produto["preco_unitario"]) * int(produto["quantidade"]) for produto in produtos)
        data_compra = datetime.now().isoformat()

        # Create purchase document
        purchase_document = {
            "_id": purchase_id,
            "user_id": user_id,
            "data_compra": data_compra,
            "valor_total": valor_total,
            "produtos": produtos,
            "endereco_entrega": {
                "rua": endereco_entrega.get("rua"),
                "bairro": endereco_entrega.get("bairro"),
                "cidade": endereco_entrega.get("cidade"),
                "estado": endereco_entrega.get("estado"),
                "numero": endereco_entrega.get("numero"),
                "complemento": endereco_entrega.get("complemento")
            },
            "status": "Processando"
        }

        # Insert purchase document
        purchases_collection = db.get_collection("purchase")
        purchases_collection.insert_one(purchase_document)
        
        print(f"Compra realizada com sucesso! ID: {purchase_id}")

        # Update user's purchases list
        compra_simplificada = {
            "id": purchase_id,
            "data_compra": data_compra,
            "valor_total": str(valor_total),
            "status": "Processando"
        }

        compras = user_data.get('compras', [])
        compras.append(compra_simplificada)

        # Update user document
        user_collection = db.get_collection("user")
        user_collection.update_one(
            {"_id": user_id},
            {"$set": {"compras": compras}}
        )

        # Update product stock and sales
        for produto in produtos:
            update_sale_and_stock(db, produto["produto_id"], int(produto["quantidade"]))
        
    except Exception as e:
        print(f"Erro ao criar compra: {e}")
