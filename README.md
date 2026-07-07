 SQLModel + SQLite - CRUD e Consultas

Projeto prático da Jornada de Dados, com foco em ORM usando **SQLModel** para
persistir e consultar dados em um banco **SQLite**.

## 🎯 O que este projeto pratica

- Criação de modelos de dados com `SQLModel`, combinando validação de tipos
  (Pydantic) com mapeamento para tabelas de banco de dados (SQLAlchemy)
- Definição de chave primária, campos obrigatórios e opcionais
- Conexão com banco de dados via `create_engine`
- Criação de tabelas automaticamente a partir dos modelos (`metadata.create_all`)
- Inserção de registros usando `Session` (`add` + `commit`)
- Execução de **SQL puro** dentro do SQLModel usando `text()`, para consultas
  mais diretas ao banco
- Leitura e exibição de resultados com `fetchall()`

## 🛠️ Tecnologias

- Python
- [SQLModel](https://sqlmodel.tiangolo.com/)
- SQLite
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências

## 📂 Estrutura

```
.
├── main.py          # Script principal: modelo, engine, sessão e consultas
├── database.db       # Banco SQLite gerado localmente
├── pyproject.toml    # Dependências do projeto (Poetry)
└── poetry.lock
```

## ▶️ Como rodar

```bash
poetry install
poetry run python main.py
```
## 💻 Exemplo de execução

```
$ poetry run python main.py
(1, 'Rusty-Man', 'Tommy Sharp', 48)
(2, 'Deadpond', 'Dive Wilson', None)
(3, 'Spider-Boy', 'Pedro Parqueador', None)


Isso cria o banco `database.db` (caso não exista), insere os registros de
exemplo e executa uma consulta `SELECT * FROM hero;` imprimindo o resultado
no terminal.

## 📝 Aprendizados

Esse projeto foi útil para entender a diferença entre trabalhar com o ORM de
forma "pura" (manipulando objetos Python que o SQLModel traduz para SQL) e
escrever SQL manualmente quando é necessário mais controle sobre a consulta.

> Parte do conteúdo da aula original inclui também uma API com FastAPI e um
> frontend em Streamlit rodando via Docker Compose — essa parte ainda está em
> progresso e será documentada em um projeto separado quando estiver
> funcionando de ponta a ponta.
# aula13_bootcamp
