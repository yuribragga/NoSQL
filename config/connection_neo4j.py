from neo4j import GraphDatabase

def connection_neo4j():
    URI = "neo4j+ssc://b135cb71.databases.neo4j.io"
    AUTH = ("neo4j", "iWnXoPPKBDWDrS8EYXBxPMV9JTDeB5AwngoztnO43ns")

    try:
        driver = GraphDatabase.driver(URI, auth=(AUTH))
        session = driver.session()
        print("Conexão com o Neo4j realizada com sucesso!")
        return driver, session
    except Exception as e:
        print(f"Erro ao conectar ao Neo4j: {e}")
        return None