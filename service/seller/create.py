from uuid import uuid4

def create_seller(db):
    try:
        seller_id = str(uuid4())
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados do novo vendedor:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        
        nome = input("Nome: ")
        email = input("Email: ")
        cnpj = input("CNPJ: ")
        avaliacao = 5.0
        
        enderecos = []
        while True:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
            rua = input("Rua: ")
            numero = input("Número: ")
            tipo_imovel = input("Tipo de imóvel: ")
            complemento = input("Complemento (deixe em branco se não houver): ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            estado = input("Estado: ")

            enderecos.append({
                "rua": rua,
                "numero": numero,
                "tipo_imovel": tipo_imovel,
                "complemento": complemento,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado
            })

            continuar = input("Deseja adicionar outro endereço? (s/n): ")
            if continuar.lower() != 's':
                break
        
        produtos = []
        
        # Create seller document
        seller_document = {
            "_id": seller_id,
            "nome": nome,
            "email": email,
            "cnpj": cnpj,
            "avaliacao": avaliacao,
            "enderecos": enderecos,
            "produtos": produtos
        }
        
        collection = db.get_collection("seller")
        collection.insert_one(seller_document)
        
        print(f"Vendedor criado com sucesso! ID: {seller_id}")
        return
    except Exception as e:
        print(f"Erro ao criar vendedor: {e}")
        return None

