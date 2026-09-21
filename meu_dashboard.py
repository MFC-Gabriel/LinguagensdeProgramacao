import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# Fase 1 - Carregamento com cache
@st.cache_data
def carregar_dados():
    df = pd.read_csv("vendas.csv")
    df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
    df["Receita"] = pd.to_numeric(df["Receita"], errors="coerce").fillna(0)
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce").fillna(0)
    return df


df = carregar_dados()

st.title("Dashboard de Vendas")

# Fase 2 - Filtros laterais
st.sidebar.title("Filtros")

lista_de_categorias = sorted(df["Categoria"].dropna().unique().tolist())

categorias_selecionadas = st.sidebar.multiselect(
    "Selecione as Categorias",
    options=lista_de_categorias,
    default=lista_de_categorias
)

# Regra de ouro: filtrar o DataFrame com base no widget
df_filtrado = df[df["Categoria"].isin(categorias_selecionadas)].copy()

# Fase 3 - Métricas
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    receita_calculada = df_filtrado["Receita"].sum()
    st.metric(label="Receita Total", value=f"R$ {receita_calculada:,.2f}")

with col2:
    # Total de PEDIDOS = Pedido_ID únicos (não somar linhas!)
    total_pedidos = df_filtrado["Pedido_ID"].nunique()
    st.metric(label="Total de Pedidos", value=f"{total_pedidos:,}")

with col3:
    # Bônus: ticket médio
    ticket_medio = receita_calculada / total_pedidos if total_pedidos else 0
    st.metric(label="Ticket Médio", value=f"R$ {ticket_medio:,.2f}")

# Fase 3 - Abas
aba1, aba2 = st.tabs(["Evolução Mensal", "Tabela de Dados"])

with aba1:
    st.subheader("Evolução Mensal da Receita")

    dados_mensais = df_filtrado.dropna(subset=["Data"]).copy()
    dados_mensais["Mês"] = dados_mensais["Data"].dt.to_period("M").astype(str)

    dados_agrupados = (
        dados_mensais
        .groupby("Mês")["Receita"]
        .sum()
        .reset_index()
        .set_index("Mês")
    )

    st.area_chart(dados_agrupados)

with aba2:
    st.subheader("Dados Filtrados")
    st.dataframe(df_filtrado, use_container_width=True)

    csv = df_filtrado.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Baixar CSV filtrado",
        data=csv,
        file_name="dados_filtrados.csv",
        mime="text/csv"
    )