from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def connection():
    uri = "mongodb+srv://yurihama:5gKAl1yBLxeSlZ08@cluster0.43xnlam.mongodb.net/"
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')  
        print("Banco conectado!")
        return client  
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None  
