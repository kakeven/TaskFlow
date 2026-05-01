# TaskFlow API

API REST para gerenciamento de tarefas com autenticação JWT, desenvolvida com FastAPI e PostgreSQL.

🔗 **Deploy:** [https://taskflow-nnno.onrender.com/docs](https://taskflow-nnno.onrender.com/docs)

---

## 🚀 Tecnologias

- **[FastAPI](https://fastapi.tiangolo.com/)** — framework web moderno e de alta performance
- **[PostgreSQL](https://www.postgresql.org/)** — banco de dados relacional
- **[SQLAlchemy](https://www.sqlalchemy.org/)** — ORM para mapeamento de dados
- **[JWT (Jose)](https://python-jose.readthedocs.io/)** — autenticação stateless via tokens
- **[Docker](https://www.docker.com/)** — containerização da aplicação
- **[Render](https://render.com/)** — plataforma de deploy

---

## ✨ Funcionalidades

- Cadastro e login de usuários
- Autenticação e autorização via JWT
- CRUD completo de tarefas
- Rotas protegidas por token

---

## 📦 Como rodar localmente

### Pré-requisitos

- Python 3.11+
- PostgreSQL ou Docker

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/taskflow.git
cd taskflow
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256

# se for usar sqlite, não coloque essa variavel
DATABASE_URL=postgresql://postgres:sua_senha@localhost:5432/taskflow
```

### 5. Rode a aplicação

```bash
uvicorn main:app --reload
```

Acesse a documentação em: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔐 Autenticação

A API utiliza autenticação via **JWT Bearer Token**.

1. Crie uma conta em `POST /auth/register`
2. Faça login em `POST /auth/login` e copie o token retornado
3. Clique em **Authorize** no Swagger e cole o token
4. A partir daí todas as rotas protegidas estarão disponíveis

---

## 📄 Endpoints

| Método | Rota | Descrição | Auth |
|--------|------|-----------|------|
| POST | `/auth/register` | Cadastro de usuário | ❌ |
| POST | `/auth/login` | Login e geração de token | ❌ |
| GET | `/tasks` | Listar tarefas do usuário | ✅ |
| POST | `/tasks` | Criar tarefa | ✅ |
| PUT | `/tasks/{id}` | Atualizar tarefa | ✅ |
| DELETE | `/tasks/{id}` | Deletar tarefa | ✅ |

> Os endpoints exatos podem variar. Consulte a [documentação interativa](https://taskflow-nnno.onrender.com/docs) para a lista completa.

---

## 🐳 Rodando com Docker

```bash
docker build -t taskflow .
docker run -p 8000:8000 --env-file .env taskflow
```

---

## 👨‍💻 Autor

Feito por **Kauã** — [LinkedIn](#) · [GitHub](#)
