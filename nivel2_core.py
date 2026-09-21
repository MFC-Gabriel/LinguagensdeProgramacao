"""
Nível 2 - Intermediário
Uso do SQLAlchemy Core: Table, MetaData, insert, update, select, func.
"""
from sqlalchemy import (
    create_engine, MetaData, Table, Column,
    Integer, String, Float, insert, update, select, func
)

engine = create_engine("sqlite:///sistema_rh.db", echo=False)
metadata = MetaData()

# ------------------------------------------------------------------
# Passo 1: Definir a tabela 'projetos' de forma programática
# ------------------------------------------------------------------
projetos = Table(
    "projetos", metadata,
    Column("id",          Integer, primary_key=True, autoincrement=True),
    Column("nome",        String(100), nullable=False),
    Column("responsavel", String(100), nullable=False),
    Column("orcamento",   Float,       nullable=False),
)

# ------------------------------------------------------------------
# Passo 1 (cont.): reaproveitar a tabela 'funcionarios' já existente
# ------------------------------------------------------------------
funcionarios = Table("funcionarios", metadata, autoload_with=engine)

# Cria fisicamente a tabela 'projetos' no banco
metadata.create_all(engine)
print("✅ Tabela 'projetos' criada/verificada.")

# ------------------------------------------------------------------
# Passo 2: Bulk insert (inserção em lote)
# ------------------------------------------------------------------
lista_projetos = [
    {"nome": "Portal do Cliente",  "responsavel": "Ana Souza",  "orcamento": 85000.0},
    {"nome": "App Mobile",         "responsavel": "Bruno Lima", "orcamento": 120000.0},
    {"nome": "Migração Cloud",     "responsavel": "Carla Dias", "orcamento": 200000.0},
    {"nome": "Data Warehouse",     "responsavel": "Diego Alves","orcamento": 150000.0},
]

with engine.begin() as conn:
    conn.execute(insert(projetos), lista_projetos)
print(f"✅ {len(lista_projetos)} projetos inseridos em lote.")

# ------------------------------------------------------------------
# Passo 3: UPDATE - reajuste salarial para 'Desenvolvedor Júnior'
# ------------------------------------------------------------------
with engine.begin() as conn:
    resultado = conn.execute(
        update(funcionarios)
        .where(funcionarios.c.cargo == "Desenvolvedor Júnior")
        .values(salario = funcionarios.c.salario * 1.10)  # +10%
    )
print(f"✅ Reajuste aplicado em {resultado.rowcount} funcionário(s).")

# ------------------------------------------------------------------
# Passo 4: Relatório agregado (média salarial por cargo)
# ------------------------------------------------------------------
consulta = (
    select(
        funcionarios.c.cargo,
        func.avg(funcionarios.c.salario).label("media_salarial"),
        func.count(funcionarios.c.id).label("qtd_funcionarios"),
    )
    .group_by(funcionarios.c.cargo)
    .order_by(funcionarios.c.cargo)
)

with engine.connect() as conn:
    linhas = conn.execute(consulta).all()

print("\n📊 Relatório — Média salarial por cargo:")
print(f"{'Cargo':<25} {'Média (R$)':>12} {'Qtd':>5}")
print("-" * 45)
for cargo, media, qtd in linhas:
    print(f"{cargo:<25} {media:>12,.2f} {qtd:>5}")