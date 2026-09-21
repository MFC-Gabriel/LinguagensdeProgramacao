"""
nivel1_basico.py
Nível 1 — Básico (URLs, Parâmetros e Cabeçalhos)
"""

import requests
from utils import HEADERS_PADRAO, TIMEOUT_PADRAO, cabecalho


def exercicio_1_1_e_1_3():
    """Requisição GET simples com headers personalizados."""
    cabecalho("Exercício 1.1 + 1.3 — GET com headers personalizados")
    url = "https://jsonplaceholder.typicode.com/posts"

    resposta = requests.get(url, headers=HEADERS_PADRAO, timeout=TIMEOUT_PADRAO)
    print(f"Status code: {resposta.status_code}")
    print(f"URL final  : {resposta.url}")
    return resposta


def exercicio_1_2():
    """Uso do argumento params para filtrar resultados."""
    cabecalho("Exercício 1.2 — Filtro via params (userId=2, limit=5)")
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": 2, "_limit": 5}

    resposta = requests.get(
        url, params=params, headers=HEADERS_PADRAO, timeout=TIMEOUT_PADRAO
    )
    print(f"Status code: {resposta.status_code}")
    print(f"URL final  : {resposta.url}")

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\nTotal de posts retornados: {len(dados)}")
        for post in dados:
            print(f"- [{post['id']}] {post['title'][:60]}...")


def exercicio_1_4():
    """Imprimir status code e URL final para confirmar sucesso."""
    cabecalho("Exercício 1.4 — Verificando status e URL final")
    url = "https://jsonplaceholder.typicode.com/posts"

    resposta = requests.get(url, headers=HEADERS_PADRAO, timeout=TIMEOUT_PADRAO)

    print(f"Status code : {resposta.status_code}  (esperado: 200)")
    print(f"URL final   : {resposta.url}")
    print(f"Sucesso?    {'✅ Sim' if resposta.status_code == 200 else '❌ Não'}")


def executar():
    exercicio_1_1_e_1_3()
    exercicio_1_2()
    exercicio_1_4()


if __name__ == "__main__":
    executar()