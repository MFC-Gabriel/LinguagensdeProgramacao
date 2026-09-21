"""
nivel2_intermediario.py
Nível 2 — Intermediário (JSON, Erros e Arquivos Binários)
"""

import requests
import pandas as pd
from utils import HEADERS_PADRAO, TIMEOUT_PADRAO, baixar_seguro, cabecalho


def exercicio_2_1():
    """Consulta 3 CEPs no ViaCEP e monta um DataFrame."""
    cabecalho("Exercício 2.1 — Consulta de CEPs no ViaCEP")

    ceps = ["01001000", "20040020", "30130010"]
    resultados = []

    for cep in ceps:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            r = requests.get(url, headers=HEADERS_PADRAO, timeout=TIMEOUT_PADRAO)
            r.raise_for_status()
            dados = r.json()

            if "erro" in dados:
                print(f"⚠ CEP {cep} não encontrado.")
                continue

            resultados.append({
                "cep":        dados.get("cep"),
                "logradouro": dados.get("logradouro"),
                "bairro":     dados.get("bairro"),
                "localidade": dados.get("localidade"),
                "uf":         dados.get("uf"),
            })
            print(f"✅ CEP {cep} consultado com sucesso.")
        except requests.RequestException as e:
            print(f"❌ Falha ao consultar {cep}: {e}")

    df = pd.DataFrame(resultados)
    print("\n📊 DataFrame resultante:")
    print(df.to_string(index=False))
    return df


def exercicio_2_2():
    """Demonstra a função de download segura (definida em utils.py)."""
    cabecalho("Exercício 2.2 — Download seguro com try/except")

    # URL válida
    ok = baixar_seguro("https://jsonplaceholder.typicode.com/posts/1")
    print(f"✅ Download válido: {'OK' if ok else 'FALHOU'}")

    # URL inválida (404) → deve cair no except
    print("\nTestando URL inexistente (espera-se erro tratado):")
    baixar_seguro("https://jsonplaceholder.typicode.com/rota-inexistente")


def exercicio_2_3():
    """Baixa uma imagem aleatória do Picsum e salva em disco."""
    cabecalho("Exercício 2.3 — Download de imagem binária (Picsum)")

    url_img = "https://picsum.photos/400/400"
    conteudo = baixar_seguro(url_img)

    if conteudo:
        caminho = "imagem_aleatoria.jpg"
        with open(caminho, "wb") as f:      # modo binário
            f.write(conteudo)
        print(f"✅ Imagem salva em: {caminho} ({len(conteudo)} bytes)")
    else:
        print("⚠ Não foi possível baixar a imagem.")


def executar():
    exercicio_2_1()
    exercicio_2_2()
    exercicio_2_3()


if __name__ == "__main__":
    executar()