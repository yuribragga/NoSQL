from astrapy import DataAPIClient
from config.create_collections import create_collection

def connection_cassandra():
    try:
        # Initialize the client
        client = DataAPIClient("AstraCS:pGimEjGnSsAArennWcGTnqRG:7ed531b2975e882158745eccd27d02760ece9ee1ac337a4d5bde10058aa815ab")
        db = client.get_database_by_api_endpoint(
            "https://08ded578-2ba3-48ca-bd8a-c2466fa7bea1-us-east-2.apps.astra.datastax.com"
        )
        
        print(f"Connected to Astra DB: {db.list_collection_names()}")
        create_collection(db)
        return db
    except Exception as e:
        print(f'Erro ao conectar ao AstraDB: {e}')
        return None
