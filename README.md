# Sistema Mercado Livre - Cassandra (AstraDB)

Sistema de gerenciamento do Mercado Livre utilizando Apache Cassandra através da plataforma AstraDB da DataStax.

## 📋 Funcionalidades

- **Gerenciamento de usuários** com autenticação
- **Cadastro e consulta de produtos**
- **Sistema de compras** e histórico
- **Gestão de vendedores**
- **Conexão com AstraDB** (Cassandra na nuvem)

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Apache Cassandra** via **AstraDB** (DataStax)
- **astrapy** - Cliente Python para AstraDB
- **cassandra-driver** - Driver Cassandra para Python

## ⚙️ Pré-requisitos

### 1. Criar Conta no AstraDB

1. Acesse [DataStax Astra](https://astra.datastax.com/)
2. Crie uma conta gratuita
3. Crie um novo **Database**
4. Anote o **Database ID** e **Region**
5. Gere um **Application Token**

### 2. Configurar Credenciais

No arquivo `config/connection_cassandra.py`, você precisa atualizar:

```python
# Substitua pelo seu Application Token
client = DataAPIClient("AstraCS:SEU_TOKEN_AQUI")

# Substitua pela URL do seu database
db = client.get_database_by_api_endpoint(
    "https://SEU_DATABASE_ID-REGION.apps.astra.datastax.com"
)
```

## 🚀 Instalação e Execução

### 1. Clone o Repositório
```bash
git clone <seu-repositorio>
cd NoSQL
```

### 2. Criar Ambiente Virtual

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

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o Sistema
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
NoSQL/
├── config/
│   ├── connection_cassandra.py    # Conexão com AstraDB
│   └── create_collections.py      # Criação das collections
├── Menu/
│   ├── product.py                 # Gerenciamento de produtos
│   ├── purchases.py               # Gerenciamento de compras
│   ├── user.py                    # Gerenciamento de usuários
│   └── seller.py                  # Gerenciamento de vendedores
├── main.py                        # Arquivo principal
└── requirements.txt               # Dependências do projeto
```

## 📦 Dependências Principais

- `astrapy>=1.5.0` - Cliente Python para AstraDB
- `cassandra-driver>=3.29.0` - Driver Cassandra
- `click>=8.0.0` - Interface de linha de comando

## 🎯 Como Usar

1. **Execute o programa:**
   ```bash
   python main.py
   ```

2. **Menu Principal:**
   - `1` - Gerenciar Cliente
   - `2` - Gerenciar Compra  
   - `3` - Gerenciar Vendedor
   - `4` - Gerenciar Produto
   - `5` - Sair

3. **Navegue pelos menus** conforme suas necessidades

## 🔧 Configuração Detalhada

### Obter Token do AstraDB

1. No painel do AstraDB, vá em **Settings > Application Tokens**
2. Clique em **Generate Token**
3. Selecione a role **Database Administrator**
4. Copie o token gerado
5. Cole no arquivo `connection_cassandra.py`

### Obter URL do Database

1. No painel do AstraDB, selecione seu database
2. Vá na aba **Connect**
3. Copie a **API Endpoint URL**
4. Cole no arquivo `connection_cassandra.py`

## ⚠️ Troubleshooting

### Erro "Failed to connect to AstraDB"
- Verifique se o token está correto
- Confirme se a URL do database está correta
- Certifique-se de que o database está ativo

### Erro "ModuleNotFoundError"
```bash
pip install astrapy cassandra-driver
```

### Collections não encontradas
- O sistema criará automaticamente as collections necessárias
- Verifique se você tem permissões adequadas no AstraDB

## 📊 Collections Criadas

O sistema criará automaticamente as seguintes collections:
- **users** - Dados dos usuários
- **products** - Catálogo de produtos  
- **purchases** - Histórico de compras
- **sellers** - Informações dos vendedores


