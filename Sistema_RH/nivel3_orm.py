"""
Nível 3 - Avançado
ORM com declarative_base, mapped_column, relationship, sessionmaker.
"""
from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import (
    declarative_base, mapped_column, relationship, sessionmaker,
    Mapped
)

engine = create_engine("sqlite:///sistema_rh.db", echo=False)
Base = declarative_base()

# ------------------------------------------------------------------
# Passo 1: Definir as classes ORM
# ------------------------------------------------------------------
class Departamento(Base):
    __tablename__ = "departamentos"

    id:    Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome:  Mapped[str] = mapped_column(nullable=False)

    # Passo 2: relacionamento 1:N
    funcionarios: Mapped[list["FuncionarioORM"]] = relationship(
        back_populates="departamento",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Departamento(id={self.id}, nome='{self.nome}')>"


class FuncionarioORM(Base):
    __tablename__ = "funcionarios_orm"

    id:             Mapped[int]   = mapped_column(primary_key=True, autoincrement=True)
    nome:           Mapped[str]   = mapped_column(nullable=False)
    cargo:          Mapped[str]   = mapped_column(nullable=False)
    salario:        Mapped[float] = mapped_column(nullable=False)
    departamento_id:Mapped[int]   = mapped_column(ForeignKey("departamentos.id"))

    # Passo 2: lado N aponta de volta para o Departamento
    departamento: Mapped["Departamento"] = relationship(back_populates="funcionarios")

    def __repr__(self):
        return (f"<FuncionarioORM(id={self.id}, nome='{self.nome}', "
                f"cargo='{self.cargo}', salario={self.salario})>")


# Cria as tabelas no banco
Base.metadata.create_all(engine)
print("✅ Tabelas ORM criadas/verificadas.")

# ------------------------------------------------------------------
# Passo 3: Sessão + persistência em cascata
# ------------------------------------------------------------------
Session = sessionmaker(bind=engine)
sessao = Session()

# Evita duplicar se rodar mais de uma vez
if sessao.query(Departamento).count() == 0:
    ti = Departamento(
        nome="TI",
        funcionarios=[
            FuncionarioORM(nome="Ana Souza",   cargo="Desenvolvedor Júnior", salario=4950.0),
            FuncionarioORM(nome="Bruno Lima",  cargo="Desenvolvedor Sênior", salario=12000.0),
            FuncionarioORM(nome="Carla Dias",  cargo="Tech Lead",            salario=15000.0),
        ],
    )
    rh = Departamento(
        nome="RH",
        funcionarios=[
            FuncionarioORM(nome="Diego Alves", cargo="Analista de RH", salario=5200.0),
        ],
    )

    sessao.add_all([ti, rh])
    sessao.commit()
    print("✅ Departamentos e funcionários persistidos.")

# ------------------------------------------------------------------
# Passo 4: Consulta orientada a objetos
# ------------------------------------------------------------------
consulta = (
    select(FuncionarioORM)
    .join(Departamento)
    .where(Departamento.nome == "TI")
)

funcionarios_ti = sessao.execute(consulta).scalars().all()

print("\n👥 Funcionários do departamento 'TI':")
for f in funcionarios_ti:
    print(f"  • {f.nome} — {f.cargo} — R$ {f.salario:,.2f}")

# Navegação objeto → objeto (relationship em ação)
print("\n🔎 Navegação via relationship:")
depto_ti = sessao.execute(
    select(Departamento).where(Departamento.nome == "TI")
).scalar_one()
print(f"  Departamento: {depto_ti.nome} "
      f"({len(depto_ti.funcionarios)} funcionários)")

# Encerrar a sessão
sessao.close()
print("\n🔒 Sessão encerrada com sucesso.")