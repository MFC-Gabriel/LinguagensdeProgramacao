"""
nivel3_avancado.py
Nível 3 — Avançado (Webscraping e Ética)
"""

import io
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from utils import HEADERS_PADRAO, TIMEOUT_PADRAO, cabecalho


def exercicio_3_1():
    """Consulta o robots.txt do site antes de raspar (ética)."""
    cabecalho("Exercício 3.1 — Verificando robots.txt (ética)")

    base = "https://books.toscrape.com/"
    r = requests.get(base + "robots.txt", headers=HEADERS_PADRAO, timeout=TIMEOUT_PADRAO)

    print(f"Status: {r.status_code}")
    if r.status_code == 200:
        print("Conteúdo do robots.txt:")
        print(r.text[:500])
    else:
        print("ℹ O site não publica robots.txt — ainda assim, usaremos "
              "requisições moderadas e identificadas.")


def exercicio_3_2():
    """Extrai título e preço dos 5 primeiros livros de books.toscrape.com."""
    cabecalho("Exercício 3.2 — Extraindo 5 livros com BeautifulSoup")

    url = "https://books.toscrape.com/"
    r = requests.get(url, headers=HEADERS_PADRAO, timeout=TIMEOUT_PADRAO)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    livros = soup.select("article.product_pod")[:5]

    dados = []
    for livro in livros:
        titulo = livro.h3.a["title"]
        preco = livro.select_one("p.price_color").text.strip()
        dados.append({"titulo": titulo, "preco": preco})

    for i, l in enumerate(dados, 1):
        print(f"{i}. {l['titulo']} — {l['preco']}")

    time.sleep(0.5)  # boa prática: pausa entre requisições
    return dados


def exercicio_3_3(dados: list[dict]):
    """Salva os dados dos livros em CSV."""
    cabecalho("Exercício 3.3 — Salvando livros em CSV")

    df = pd.DataFrame(dados)
    caminho = "livros.csv"
    df.to_csv(caminho, index=False, encoding="utf-8")
    print(f"✅ Arquivo salvo: {caminho}")
    print(df.to_string(index=False))


def exercicio_3_4():
    """Lê tabela de uma página da Wikipédia com pandas.read_html + io.StringIO."""
    cabecalho("Exercício 3.4 — Tabela da Wikipédia com read_html")

    url = "https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o"
    r = requests.get(url, headers=HEADERS_PADRAO, timeout=TIMEOUT_PADRAO)
    r.raise_for_status()

    tabelas = pd.read_html(io.StringIO(r.text))
    print(f"Total de tabelas encontradas: {len(tabelas)}")

    df = tabelas[0]
    print("\n📊 Primeiras linhas:")
    print(df.head(10).to_string(index=False))

    df.to_csv("paises_populacao.csv", index=False, encoding="utf-8")
    print("\n✅ Arquivo salvo: paises_populacao.csv")
    return df


def executar():
    exercicio_3_1()
    dados = exercicio_3_2()
    exercicio_3_3(dados)
    exercicio_3_4()


if __name__ == "__main__":
    executar()