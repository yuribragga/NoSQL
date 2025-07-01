from uuid import uuid4

def create_user(db):
    try:
        user_id = str(uuid4())
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        print("Informe os dados do novo usuário:")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-")
        nome = input("Nome: ")
        email = input("Email: ")
        cpf = input("CPF: ")
        senha = input("Senha: ")
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

        favoritos = []
        compras = []
        
        # Create user document
        user_document = {
            "_id": user_id,
            "nome": nome,
            "email": email,
            "cpf": cpf,
            "senha": senha,
            "enderecos": enderecos,
            "favoritos": favoritos,
            "compras": compras
        }
        
        collection = db.get_collection("user")
        collection.insert_one(user_document)
        
        print(f"Usuário criado com sucesso! ID: {user_id}")
        return 
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None
