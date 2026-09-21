"""
Nível 1 - Básico
Conexão com SQLite + SQL nativo com parâmetros seguros (anti SQL Injection).
"""
import pandas as pd
from sqlalchemy import create_engine, text

# ------------------------------------------------------------------
# Passo 1: Conexão com o banco local
# ------------------------------------------------------------------
engine = create_engine("sqlite:///sistema_rh.db", echo=False)

# ------------------------------------------------------------------
# Passo 2: Criar a tabela 'funcionarios' com SQL puro (DDL)
# ------------------------------------------------------------------
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS funcionarios (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nome    TEXT    NOT NULL,
            cargo   TEXT    NOT NULL,
            salario REAL    NOT NULL
        )
    """))
print("✅ Tabela 'funcionarios' criada/verificada.")

# ------------------------------------------------------------------
# Passo 3: INSERT com parâmetros seguros (placeholders)
# ------------------------------------------------------------------
# Simula dados vindos de um formulário web
formulario_web = {
    "nome":    "Ana Souza",
    "cargo":   "Desenvolvedor Júnior",
    "salario": 4500.00,
}

with engine.begin() as conn:
    conn.execute(
        text("""
            INSERT INTO funcionarios (nome, cargo, salario)
            VALUES (:nome, :cargo, :salario)
        """),
        formulario_web,   # dicionário com os valores
    )
print(f"✅ Funcionário '{formulario_web['nome']}' inserido com segurança.")

# ------------------------------------------------------------------
# Passo 4: Validar a inserção com pandas
# ------------------------------------------------------------------
df = pd.read_sql_query("SELECT * FROM funcionarios", engine)
print("\n📋 Conteúdo atual da tabela 'funcionarios':")
print(df)

# ------------------------------------------------------------------
# 🧠 Pergunta reflexiva (resposta comentada)
# ------------------------------------------------------------------
"""
Por que NÃO concatenar strings no SQL?

Se fizéssemos:
    sql = f"INSERT INTO funcionarios (nome) VALUES ('{nome_digitado}')"

E o usuário digitasse:
    '); DROP TABLE funcionarios; --

O banco receberia DUAS instruções: um INSERT e um DROP TABLE.
Isso é SQL Injection.

Com placeholders (:nome, :cargo), o SQLAlchemy envia o comando
e os valores SEPARADAMENTE para o driver do banco. O banco trata
o valor como DADO, nunca como código SQL. Assim, mesmo que o
usuário digite '); DROP TABLE ...', isso será salvo apenas como
uma string inofensiva no campo 'nome'.
"""