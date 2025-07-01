# Utility functions for AstraDB document operations

def convert_ordered_map_to_dict(ordered_map):
    """Convert ordered map to dict - now just returns the input since we're using documents"""
    return ordered_map if ordered_map else {}

def row_to_dict_user(document):
    """Convert user document to dict format"""
    if not document:
        return {}
    return {
        "id": str(document.get("_id", "")), 
        "compras": document.get("compras", []),
        "cpf": document.get("cpf", ""),
        "email": document.get("email", ""),
        "enderecos": document.get("enderecos", []),
        "favoritos": document.get("favoritos", []),
        "nome": document.get("nome", ""),
        "senha": document.get("senha", ""),
    }

def row_to_dict_seller(document):
    """Convert seller document to dict format"""
    if not document:
        return {}
    return {
        "id": str(document.get("_id", "")),  
        "nome": document.get("nome", ""), 
        "email": document.get("email", ""), 
        "cnpj": document.get("cnpj", ""),  
        "avaliacao": document.get("avaliacao", 0.0),  
        "enderecos": document.get("enderecos", []), 
        "produtos": document.get("produtos", []), 
    }

def row_to_dict_purchase(document):
    """Convert purchase document to dict format"""
    if not document:
        return {}
    return {
        "id": str(document.get("_id", "")), 
        "data_compra": document.get("data_compra", ""),  
        "valor_total": document.get("valor_total", 0.0),
        "status": document.get("status", ""),  
        "user_id": document.get("user_id", ""),
        "endereco_entrega": document.get("endereco_entrega", {}),
        "produtos": document.get("produtos", [])
    }

def get_product(db, product_id):
    """Get a single product by ID"""
    try:
        collection = db.get_collection("products")
        product = collection.find_one({"_id": product_id})
        return product
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
        return None

def get_seller(db, seller_id):
    """Get a single seller by ID"""
    try:
        collection = db.get_collection("seller")
        seller = collection.find_one({"_id": seller_id})
        return seller
    except Exception as e:
        print(f"Erro ao buscar vendedor: {e}")
        return None

def get_purchase(db, purchase_id):
    """Get a single purchase by ID"""
    try:
        collection = db.get_collection("purchase")
        purchase = collection.find_one({"_id": purchase_id})
        return purchase
    except Exception as e:
        print(f"Erro ao buscar compra: {e}")
        return None

def get_user(db, user_id):
    """Get a single user by ID"""
    try:
        collection = db.get_collection("user")
        user = collection.find_one({"_id": user_id})
        return user
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None

def get_all_users(db):
    """Get all users from the collection"""
    try:
        collection = db.get_collection("user")
        users = list(collection.find())
        return users
    except Exception as e:
        print(f"Erro ao buscar usuários: {e}")
        return []

def get_all_sellers(db):
    """Get all sellers from the collection"""
    try:
        collection = db.get_collection("seller")
        sellers = list(collection.find())
        return sellers
    except Exception as e:
        print(f"Erro ao buscar vendedores: {e}")
        return []

def get_all_purchases(db):
    """Get all purchases from the collection"""
    try:
        collection = db.get_collection("purchase")
        purchases = list(collection.find())
        return purchases
    except Exception as e:
        print(f"Erro ao buscar compras: {e}")
        return []

def get_all_products(db):
    """Get all products from the collection"""
    try:
        collection = db.get_collection("products")
        products = list(collection.find())
        return products
    except Exception as e:
        print(f"Erro ao buscar produtos: {e}")
        return []

def list_users(db):
    """List all users with formatted output"""
    users = get_all_users(db)
    if not users:
        print("Nenhum usuário cadastrado.")
        return None
    for user in users:
        user_dict = row_to_dict_user(user)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {user_dict['id']}")
        print(f"| Nome: {user_dict['nome']}")
        print(f"| E-mail: {user_dict['email']}")
    return users

def list_sellers(db):
    """List all sellers with formatted output"""
    sellers = get_all_sellers(db)
    if not sellers:
        print("Nenhum vendedor cadastrado.")
        return None
    for seller in sellers:
        seller_dict = row_to_dict_seller(seller)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {seller_dict['id']}")
        print(f"| Nome: {seller_dict['nome']}")
        print(f"| E-mail: {seller_dict['email']}")
    return sellers

def list_purchases(db):
    """List all purchases with formatted output"""
    purchases = get_all_purchases(db)
    if not purchases:
        print("Nenhuma compra cadastrada.")
        return None
    for purchase in purchases:
        purchase_dict = row_to_dict_purchase(purchase)
        user = get_user(db, purchase_dict['user_id'])
        user_dict = row_to_dict_user(user)
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {purchase_dict['id']}")
        print(f"| Data: {purchase_dict['data_compra']}")
        print(f"| Valor: R${purchase_dict['valor_total']}")
        print(f"| Comprador: {user_dict['nome']}")
    return purchases

def list_products(db):
    """List all products with formatted output"""
    products = get_all_products(db)
    if not products:
        print("Nenhum produto cadastrado.")
        return None
    for product in products:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {product.get('_id', '')}")
        print(f"| Nome: {product.get('nome_produto', '')}")
        print(f"| Valor: R${product.get('valor', 0.0):.2f}")
        print(f"| Vendedor: {product.get('nome_vendedor', '')}")
    return products

def update_sale_and_stock(db, product_id, quantity):
    """Update product stock and sales count"""
    try:
        collection = db.get_collection("products")
        product = collection.find_one({"_id": product_id})
        
        if not product:
            print(f"Produto não encontrado.")
            return
            
        estoque = product.get("estoque", 0)
        vendas = product.get("vendas", 0)
        
        new_estoque = estoque - quantity
        new_vendas = vendas + quantity
        
        collection.update_one(
            {"_id": product_id},
            {"$set": {"estoque": new_estoque, "vendas": new_vendas}}
        )
        
    except Exception as e:
        print(f"Erro ao atualizar produto: {e}")

