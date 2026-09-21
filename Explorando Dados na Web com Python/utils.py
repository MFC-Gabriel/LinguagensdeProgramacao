"""
utils.py
Funções auxiliares compartilhadas entre os níveis da atividade.
"""

import requests

# Cabeçalho padrão identificando o projeto (boa prática de scraping ético)
HEADERS_PADRAO = {
    "User-Agent": "MeuProjetoExplorandoDados/1.0 (contato@exemplo.com)"
}

TIMEOUT_PADRAO = 10


def baixar_seguro(url: str, timeout: int = TIMEOUT_PADRAO, headers: dict | None = None):
    """
    Faz uma requisição GET segura e retorna o conteúdo bruto (bytes)
    ou None em caso de falha. Trata erros HTTP, de conexão e timeout.
    """
    try:
        resposta = requests.get(
            url,
            timeout=timeout,
            headers=headers or HEADERS_PADRAO,
        )
        resposta.raise_for_status()
        return resposta.content
    except requests.HTTPError as e:
        print(f"❌ Erro HTTP ({e.response.status_code}) ao acessar {url}")
    except requests.ConnectionError:
        print(f"❌ Falha de conexão com {url}")
    except requests.Timeout:
        print(f"⏱ Timeout ao acessar {url}")
    except requests.RequestException as e:
        print(f"❌ Erro inesperado: {e}")
    return None


def cabecalho(titulo: str) -> None:
    """Imprime um cabeçalho formatado no terminal."""
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)