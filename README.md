# Sistema Mercado Livre - MongoDB e Redis

Sistema de gerenciamento do Mercado Livre utilizando bancos de dados NoSQL (MongoDB para dados principais e Redis para cache/sessões).

## 📋 Funcionalidades

- **Autenticação de usuários** com controle de sessão
- **Gerenciamento de favoritos** de produtos
- **Sistema de compras** e histórico
- **Cache inteligente** com Redis
- **Persistência de dados** com MongoDB

## 🚀 Configuração do Projeto

### Clone o projeto e acesse a branch `Ex3`
```bash
git clone https://github.com/yuribragga/NoSQL-BD.git
cd NoSQL-BD
git checkout Ex3
```

## ⚙️ 1. Configuração do MongoDB

### 1.1 Criar Conta no MongoDB Atlas

- Acesse o [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) e crie uma conta ou faça login
- Crie um novo **cluster** e configure o banco de dados conforme as instruções
- No painel do MongoDB Atlas, vá em **Connect** e gere a **URI de Conexão**
- Anote as credenciais: `username`, `password` e `cluster URL`

### 1.2 Configurar connection_mongo.py

No arquivo `config/connection_mongo.py`, substitua a URI de conexão:

```python
def connection_mongo():
    # Substitua com suas credenciais reais
    uri = "mongodb+srv://SEU_USERNAME:SUA_SENHA@SEU_CLUSTER.mongodb.net/"
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    try:
        client.admin.command('ping')  
        print("Mongo conectado!")
        return client  
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None
```

## 🔴 2. Configuração do Redis

### 2.1 Criar Conta no Redis Cloud

- Acesse [Redis Cloud](https://redis.com/redis-cloud/) e crie uma conta gratuita
- Após a criação, crie um novo **banco de dados Redis**
- Obtenha as credenciais: `host`, `port`, `username` e `password`

### 2.2 Configurar connection_redis.py

No arquivo `config/connection_redis.py`, substitua as credenciais:

```python
def connection_redis():
    try:
        r = redis.Redis(
            host='SEU_HOST_REDIS',
            port=SEU_PORT,
            decode_responses=True,
            username="SEU_USERNAME",
            password="SUA_SENHA",
        )
        r.ping()
        print('Redis conectado!')
        return r 
    except redis.ConnectionError:
        print('Erro ao conectar ao Redis')
        return None
    except Exception as e:
        print(f'Ocorreu um erro: {e}')  
        return None
```

## 🛠️ 3. Instalação das Dependências

### 3.1 Criar Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3.2 Instalar Dependências

Com o ambiente virtual ativado:
```bash
pip install -r requirements.txt
```

## 🎯 4. Executar o Projeto

```bash
python main.py
```

## 📁 Estrutura do Projeto

```
NoSQL/
├── config/
│   ├── connection_mongo.py    # Conexão com MongoDB
│   └── connection_redis.py    # Conexão com Redis
├── Menu/
│   ├── favorites.py          # Gerenciamento de favoritos
│   └── purchases.py          # Gerenciamento de compras
├── service/
│   └── auth.py              # Autenticação de usuários
├── main.py                  # Arquivo principal
└── requirements.txt         # Dependências do projeto
```

## 📦 Dependências Principais

```
pymongo>=4.0.0
redis>=6.0.0
dnspython>=2.0.0
```

## 📝 Como Usar

1. Execute o programa: `python main.py`
2. Digite seu **email** e **senha** quando solicitado
3. Navegue pelos menus:
   - **1** - Gerenciar Favoritos
   - **2** - Gerenciar Compras
   - **0** - Sair do sistema

## ⚠️ Troubleshooting

### Erro "ModuleNotFoundError"
```bash
pip install pymongo redis dnspython
```

### Erro "Usuario não encontrado"
- Certifique-se de ter usuários cadastrados no MongoDB
- Verifique se a coleção `userCol` existe no banco `MercadoLivre`

### Erro de Conexão MongoDB
- Verifique a URI de conexão no `connection_mongo.py`
- Confirme se o cluster MongoDB está ativo
- Certifique-se de que seu IP está na whitelist do MongoDB Atlas

### Erro de Conexão Redis
- Verifique as credenciais no `connection_redis.py`
- Confirme se o banco Redis está ativo
- Teste a conectividade de rede

## 🔐 Segurança

- ⚠️ **Nunca commite credenciais reais** nos arquivos de configuração
- Use variáveis de ambiente para credenciais sensíveis
- Mantenha suas senhas seguras
