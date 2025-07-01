from uuid import uuid4
from utils.utils import get_seller, row_to_dict_seller

def create_product(db, seller_id):
    try:
        product_id = str(uuid4())
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados do novo produto:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")

        seller = get_seller(db, seller_id)
        if seller is None:
            print("Vendedor não encontrado!")
            return
        
        nome_produto = input("Digite o nome do produto: ")
        marca_produto = input("Digite a marca do produto: ")
        valor = float(input("Digite o valor do produto: "))
        estoque = int(input("Digite o estoque disponível: "))

        seller_data = row_to_dict_seller(seller)
        
        # Create product document
        produto_document = {
            "_id": product_id,
            "nome_produto": nome_produto,
            "marca_produto": marca_produto,
            "valor": valor,
            "estoque": estoque,
            "vendas": 0,
            "vendedor_id": seller_id,
            "nome_vendedor": seller_data["nome"],
            "email_vendedor": seller_data["email"],
            "cnpj_vendedor": seller_data["cnpj"]
        }

        # Insert product into products collection
        products_collection = db.get_collection("products")
        products_collection.insert_one(produto_document)

        # Update seller's products list
        produto_map = {
            "id": product_id,
            "nome_produto": nome_produto,
            "marca_produto": marca_produto,
            "valor": str(valor),
            "estoque": str(estoque),
            "vendas": "0",
            "vendedor_id": seller_id,
            "nome_vendedor": seller_data["nome"],
            "email_vendedor": seller_data["email"],
            "cnpj_vendedor": seller_data["cnpj"]
        }

        produtos = seller_data.get('produtos', [])
        produtos.append(produto_map)

        # Update seller document
        seller_collection = db.get_collection("seller")
        seller_collection.update_one(
            {"_id": seller_id},
            {"$set": {"produtos": produtos}}
        )

        print(f"Produto adicionado à lista de produtos do vendedor {seller_data['nome']}.")
        print(f"Produto '{nome_produto}' criado com sucesso! ID: {product_id}")

        return 
        
    except Exception as e:
        print(f"Erro ao criar produto: {e}")
        return None
