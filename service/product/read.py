from utils.utils import get_product

def read_product(db, product_id):
    try:
        product = get_product(db, product_id)
        if not product:
            print("Produto não encontrado!")
            return

        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| ID: {product.get('_id', '')}")
        print(f"| Nome: {product.get('nome_produto', '')}")
        print(f"| Marca: {product.get('marca_produto', '')}")
        print(f"| Preço: R${product.get('valor', 0.0):.2f}")
        print(f"| Estoque: {product.get('estoque', 0)}")
        print(f"| Vendas: {product.get('vendas', 0)}")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(" Informações do Vendedor:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print(f"| Nome do Vendedor: {product.get('nome_vendedor', '')}")
        print(f"| Email do Vendedor: {product.get('email_vendedor', '')}")
        print(f"| CNPJ do Vendedor: {product.get('cnpj_vendedor', '')}")
        
    except Exception as e:
        print(f"Erro ao buscar o produto: {e}")
