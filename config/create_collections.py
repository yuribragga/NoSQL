def create_collection(db):
    try:
        # Create collections in AstraDB (document-based approach)
        # Collections are created automatically when first document is inserted
        # But we can explicitly create them with schemas if needed
        
        collections_to_create = ["user", "purchase", "seller", "products"]
        
        existing_collections = db.list_collection_names()
        
        for collection_name in collections_to_create:
            if collection_name not in existing_collections:
                # Create collection - AstraDB creates collections automatically
                # when you first insert a document, but we can create them explicitly
                collection = db.create_collection(collection_name)
                print(f"Coleção '{collection_name}' criada com sucesso.")
            else:
                print(f"Coleção '{collection_name}' já existe.")
        
        print("Todas as coleções foram verificadas/criadas com sucesso.")
    except Exception as e:
        print(f'Erro ao criar coleções: {e}')
