"""
=====================================================================
 ATIVIDADE PRÁTICA — ANÁLISE DE DADOS NO VAREJO COM NUMPY
 + ORGANIZAÇÃO E TRANSFORMAÇÃO DE DADOS COM NUMPY
=====================================================================
 Um único arquivo com as soluções dos 3 níveis de cada atividade.
 Basta rodar:  python analise_varejo_numpy.py
=====================================================================
"""

import numpy as np

# Deixa a saída do NumPy mais legível (sem notação científica)
np.set_printoptions(precision=2, suppress=True)

LINHA = "=" * 70


def titulo(texto: str) -> None:
    print(f"\n{LINHA}\n{texto}\n{LINHA}")


# =====================================================================
# ATIVIDADE 1 — ANÁLISE DE DADOS NO VAREJO
# =====================================================================
titulo("ATIVIDADE 1 — ANÁLISE DE DADOS NO VAREJO")

# ---------------------------------------------------------------------
# NÍVEL 1 — Faturamento Semanal e Filtros
# ---------------------------------------------------------------------
titulo("NÍVEL 1 — Faturamento Semanal e Filtros")

# Passo 1: array 1D com as peças vendidas na semana
pecas_vendidas = np.array([150, 120, 90, 210, 300, 250, 180])
print("Peças vendidas na semana:", pecas_vendidas)

# Passo 2: faturamento (operação vetorizada — sem laço for!)
preco_medio = 50.00
faturamento = pecas_vendidas * preco_medio
print("\nFaturamento diário (R$):", faturamento)
print(f"Faturamento total da semana: R$ {faturamento.sum():,.2f}")

# Passo 3: máscara booleana para dias com mais de 200 peças
mascara_pico = pecas_vendidas > 200
dias_pico = pecas_vendidas[mascara_pico]
print("\nMáscara booleana (vendas > 200):", mascara_pico)
print("Dias de pico (valores):", dias_pico)
print("Índices dos dias de pico:", np.where(mascara_pico)[0])


# ---------------------------------------------------------------------
# NÍVEL 2 — Múltiplas Filiais e Falhas de Sistema
# ---------------------------------------------------------------------
titulo("NÍVEL 2 — Múltiplas Filiais e Falhas de Sistema")

# Passo 1: matriz 2D (lojas nas linhas, dias nas colunas)
vendas = np.array([
    [200, 220, np.nan, 250],   # Loja A — falha no 3º dia
    [150, 180, 160,    190],   # Loja B
    [300, 310, 290,    330],   # Loja C
])
print("Matriz de vendas (linhas = lojas, colunas = dias):")
print(vendas)

# Passo 2: total por loja (agregando pelas linhas -> axis=1)
# np.nansum ignora NaN; se usar .sum(axis=1) o total da Loja A vira NaN
total_por_loja = np.nansum(vendas, axis=1)
print("\nTotal de peças por loja:", total_por_loja)
for i, total in enumerate(total_por_loja):
    print(f"  Loja {chr(65 + i)}: {int(total)} peças")

# Passo 3: média diária geral ignorando NaN
media_com_nan = np.mean(vendas)          # contaminada pelo NaN
media_correta = np.nanmean(vendas)       # ignora NaN
print(f"\nMédia diária (com NaN, ERRADA): {media_com_nan}")
print(f"Média diária (nanmean, CORRETA): {media_correta:.2f}")

# Passo 4: matriz condicional com np.where
meta = 200
matriz_status = np.where(
    np.isnan(vendas),
    "Sem dados",
    np.where(vendas >= meta, "Meta Atingida", "Abaixo")
)
print("\nStatus por loja/dia (meta = 200 peças):")
for i, linha in enumerate(matriz_status):
    print(f"  Loja {chr(65 + i)}: {linha}")


# ---------------------------------------------------------------------
# NÍVEL 3 — Categorização e Destaques de Marketing
# ---------------------------------------------------------------------
titulo("NÍVEL 3 — Categorização e Destaques de Marketing")

# Passo 1: gerador moderno com semente fixa (reprodutível)
rng = np.random.default_rng(seed=42)
categorias = ["Eletrônicos", "Roupas", "Casa"]
amostra = rng.choice(categorias, size=50)
print("Amostra de 50 vendas (primeiras 10):", amostra[:10], "...")

# Passo 2: contagem por categoria com np.unique
valores, contagens = np.unique(amostra, return_counts=True)
print("\nVolume de vendas por departamento:")
for v, c in zip(valores, contagens):
    print(f"  {v:<15} -> {c} vendas")

# Passo 3: campanha campeã (índice do maior valor)
faturamento_campanhas = np.array([12000, 45000, 23000, 89000, 31000])
indice_campea = np.argmax(faturamento_campanhas)
print("\nFaturamento das campanhas:", faturamento_campanhas)
print(f"Campanha campeã: índice {indice_campea} "
      f"(R$ {faturamento_campanhas[indice_campea]:,.2f})")


# =====================================================================
# ATIVIDADE 2 — ORGANIZAÇÃO E TRANSFORMAÇÃO DE DADOS
# =====================================================================
titulo("ATIVIDADE 2 — ORGANIZAÇÃO E TRANSFORMAÇÃO DE DADOS")

# ---------------------------------------------------------------------
# NÍVEL 1 — Geração de Sequências e Tipagem
# ---------------------------------------------------------------------
titulo("NÍVEL 1 — Geração de Sequências e Tipagem")

# Passo 1: 30 dias do mês
dias_mes = np.arange(1, 31)
print("Dias do mês:", dias_mes)

# Passo 2: 5 metas igualmente espaçadas
metas = np.linspace(20000, 30000, 5)
print("\n5 metas igualmente espaçadas (R$):", metas)

# Passo 3: conversão de float para int
estoque_float = np.array([10.5, 20.1, 30.9])
estoque_int = estoque_float.astype(int)
print("\nEstoque float:", estoque_float)
print("Estoque int  :", estoque_int)

# Passo 4: últimos 5 dias em ordem inversa
ultimos_5_invertidos = dias_mes[-5:][::-1]
print("\nÚltimos 5 dias (mais recente -> mais antigo):", ultimos_5_invertidos)


# ---------------------------------------------------------------------
# NÍVEL 2 — Redimensionamento e Proteção de Dados
# ---------------------------------------------------------------------
titulo("NÍVEL 2 — Redimensionamento e Proteção de Dados")

# Passo 1: reshape (12 meses -> 4 trimestres x 3 meses)
visitas = np.arange(1200, 2400, 100)  # 12 valores fictícios
print("Array original (12 meses):", visitas)
visitas_trimestres = visitas.reshape(4, 3)
print("\nReshape (4 trimestres x 3 meses):")
print(visitas_trimestres)

# Passo 2: vstack (1º semestre + 2º semestre)
primeiro_semestre = visitas_trimestres[:2]   # 2 primeiros trimestres
segundo_semestre  = visitas_trimestres[2:]   # 2 últimos
visitas_ano = np.vstack([primeiro_semestre, segundo_semestre])
print("\nEmpilhamento vertical (ano completo):")
print(visitas_ano)

# Passo 3: fatiamento protegido com .copy()
primeiro_trimestre = visitas_ano[0:1].copy()
primeiro_trimestre[0, 0] = 9999   # altera APENAS a cópia
print("\nPrimeiro trimestre (cópia alterada para teste):")
print(primeiro_trimestre)
print("Matriz original intacta?",
      "SIM ✅" if visitas_ano[0, 0] != 9999 else "NÃO ❌")

# Passo 4: ravel (achatar de volta para 1D)
visitas_flat = visitas_ano.ravel()
print("\nArray achatado com ravel():", visitas_flat)
print("Shape final:", visitas_flat.shape)


# ---------------------------------------------------------------------
# NÍVEL 3 — Ranking, Broadcasting e Sistemas Lineares
# ---------------------------------------------------------------------
titulo("NÍVEL 3 — Ranking, Broadcasting e Sistemas Lineares")

# Passo 1: ranking com argsort
pontuacoes = np.array([85, 92, 78, 95, 88])
print("Pontuações:", pontuacoes)
indices_ordenados = np.argsort(pontuacoes)
print("Índices (argsort, crescente):", indices_ordenados)
print("Ranking do melhor para o pior:")
for pos, idx in enumerate(indices_ordenados[::-1], start=1):
    print(f"  {pos}º lugar -> Aluno {idx} (nota {pontuacoes[idx]})")

# Passo 2: newaxis + broadcasting
precos_base = np.array([100, 250, 80])          # formato (3,) - linha
precos_coluna = precos_base[:, np.newaxis]      # formato (3,1) - coluna
descontos = np.array([0.05, 0.10, 0.20])        # 3 percentuais
precos_com_desconto = precos_coluna * (1 - descontos)
print("\nPreços base (coluna):")
print(precos_coluna)
print("Descontos aplicados:", descontos)
print("\nMatriz (linhas = produtos, colunas = descontos):")
print(precos_com_desconto)

# Passo 3: sistema linear (custo de placa e sensor)
# 2 placas + 1 sensor = 500
# 1 placa  - 1 sensor = 100   (o sensor devolvido vira estorno, sinal negativo)
A = np.array([
    [2,  1],
    [1, -1],
])
b = np.array([500, 100])
solucao = np.linalg.solve(A, b)
print("\nSistema linear:")
print("  2P + 1S = 500")
print("  1P - 1S = 100")
print(f"\nPreço da placa robótica:  R$ {solucao[0]:.2f}")
print(f"Preço do sensor:          R$ {solucao[1]:.2f}")

# Validação
print("\nVerificação:")
print(f"  2*{solucao[0]:.2f} + 1*{solucao[1]:.2f} = "
      f"{2 * solucao[0] + solucao[1]:.2f}  (esperado: 500)")
print(f"  1*{solucao[0]:.2f} - 1*{solucao[1]:.2f} = "
      f"{solucao[0] - solucao[1]:.2f}  (esperado: 100)")

# Encerramento
titulo("✅ Todas as atividades foram concluídas com sucesso!")