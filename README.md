# Sistema Mercado Livre - Banco de Dados Não Relacional

Este projeto implementa um sistema de "Mercado Livre" utilizando diferentes bancos de dados não relacionais, com foco em operações CRUD (Create, Read, Update, Delete) para as entidades: Usuário, Vendedor, Produto e Compra.

## 🚀 Projeto Atual: Neo4j (Banco de Grafos)

O projeto atual utiliza **Neo4j** como banco de dados de grafos para modelar as relações entre usuários, vendedores, produtos e compras.

### 📋 Funcionalidades Implementadas:
- ✅ **Create**: Criação de usuários, vendedores, produtos e compras
- ✅ **Read**: Consulta e listagem de dados
- 🔄 **Update**: Atualização de registros (em desenvolvimento)
- 🔄 **Delete**: Remoção de registros (em desenvolvimento)

### 🛠️ Tecnologias:
- **Python 3.10+**
- **Neo4j** (Banco de grafos)
- **neo4j-driver** (Driver oficial Python)

### 📁 Estrutura do Projeto:
```
├── main.py                 # Aplicação principal
├── config/
│   └── connection_neo4j.py # Configuração de conexão
├── menu/                   # Interfaces de usuário
│   ├── user.py
│   ├── seller.py
│   ├── product.py
│   └── purchase.py
├── service/                # Lógica de negócio
│   ├── user/
│   ├── seller/
│   ├── product/
│   └── purchase/
└── utils/
    └── utils.py           # Funções utilitárias
```

### 🔗 Modelo de Dados (Grafo):
```
(User)-[:COMPROU]->(Purchase)-[:INCLUI]->(Product)<-[:VENDE]-(Seller)
```

## 📚 Outras Atividades do Curso

### ATV - II: MongoDB

> Implementar em Python as funções de manipulação da Base de Dados Não Relacional do Mercado Livre 
- Insert em todas as coleções
- Update em todas as coleções
- Search em todas as coleções
- Delete em todas as coleções

### ATV - III: MongoDB + Redis

> Implementar em Python a transferência de dados entre MongoDB e Redis
- Retirar 3 itens do MongoDB e transferir para o Redis
- Manipular os itens no Redis
- Devolver os itens para o MongoDB
- Um dos 3 itens pode ser uma nova implementação

### ATV - IV: Cassandra

> Implementar em Python as funções de manipulação no Cassandra
- **Requisito**: Utilizar COLUNAS, não pode utilizar JSON
- Insert em todas as coleções (Usuário, Vendedor, Produto, Compra)
- Update em Usuário
- Search em Produto
- Delete em Compra

## 🚀 Como Executar

### Pré-requisitos:
```bash
# Python 3.10 ou superior
pip install -r requirements.txt
```

### Configuração do Neo4j:
1. Acesse [Neo4j Aura](https://console.neo4j.io/)
2. Crie ou ative seu banco de dados
3. Atualize as credenciais em `config/connection_neo4j.py`

### Executar a Aplicação:
```bash
python main.py
```

## 📝 Dependências

```
neo4j>=5.0.0
```

## 🔧 Resolução de Problemas

Se encontrar erro "Unable to retrieve routing information":
1. Verifique se o banco Neo4j está ativo
2. Confirme as credenciais
3. Teste a conectividade com a internet
4. Verifique configurações de firewall

## 👥 Entidades do Sistema

### User (Usuário)
- Nome, Email, CPF, Senha

### Seller (Vendedor)  
- Nome, Email, CNPJ, Telefone

### Product (Produto)
- Nome, Preço, Marca
- Relacionamento: (Seller)-[:VENDE]->(Product)

### Purchase (Compra)
- Data, Valor Total, Status
- Relacionamentos: 
  - (User)-[:COMPROU]->(Purchase)
  - (Purchase)-[:INCLUI]->(Product)


