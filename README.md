# 📦 Sistema de Gerenciamento de Estoque

## 📌 Descrição
Este é um sistema para o gerenciamento de estoque de pequenos comércios, permitindo cadastro de produtos, controle automatizado de estoque, criação de ofertas para produtos próximos ao vencimento e relatórios detalhados de vendas.

## 🚀 Tecnologias Utilizadas
- **Back-end:** Python, Django, Django Rest Framework
- **Banco de Dados:** MySQL
- **Front-end:** (A definir) React/HTML, CSS, JavaScript

## 🔧 Configuração do Ambiente
### 1. Clone o repositório
```bash
git clone https://github.com/LorranFont/Project-Dashboard.git
cd Project-Dashboard
```

### 2. Crie um ambiente virtual e ative-o
```bash
python -m venv venv
# Ativar no Windows
venv\Scripts\activate
# Ativar no Linux/macOS
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
- Certifique-se de que o MySQL está rodando.
- Atualize as configurações do banco no `settings.py`.

### 5. Rode as migrações
```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional, para acessar o admin do Django)
```bash
python manage.py createsuperuser
```

### 7. Rode o servidor
```bash
python manage.py runserver
```

Acesse no navegador: `http://127.0.0.1:8000/`

## 📂 Modelos Principais
- **Produto**: Nome, validade, quantidade, preço
- **Estoque**: Atualização automática com base em entradas/saídas
- **Venda**: Registra compras e clientes
- **Oferta**: Cria ofertas automáticas para produtos próximos ao vencimento

## 🛠 Futuras Implementações
- 📊 Relatórios sobre vendas, perdas e itens mais vendidos
- 📢 Notificação de validade curta
- 🔑 Autenticação de usuários

## 📜 Licença
Este projeto está licenciado sob a MIT License - veja o arquivo `LICENSE` para mais detalhes.

