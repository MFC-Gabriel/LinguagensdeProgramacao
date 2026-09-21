# Explorando Dados na Web com Python

Atividade prática dividida em 3 níveis: básico, intermediário e avançado.

## 📦 Instalação

```bash
# (Opcional) criar ambiente virtual
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## ▶ Como executar

**Tudo de uma vez:**
```bash
python main.py
```

**Cada nível separadamente:**
```bash
python nivel1_basico.py
python nivel2_intermediario.py
python nivel3_avancado.py
```

## 📂 Arquivos gerados

Após a execução, você verá na pasta:

| Arquivo | Origem |
|---|---|
| `imagem_aleatoria.jpg` | Exercício 2.3 (Picsum) |
| `livros.csv` | Exercício 3.3 (books.toscrape.com) |
| `paises_populacao.csv` | Exercício 3.4 (Wikipédia) |

## ✅ Boas práticas adotadas

- `timeout` em todas as requisições
- `User-Agent` identificável
- Tratamento de erros com `try/except` + `raise_for_status()`
- Leitura prévia do `robots.txt`
- Pequenas pausas (`time.sleep`) entre requisições de scraping
- Escrita binária (`'wb'`) para imagens
- CSV salvo em `utf-8`

## 🧩 Estrutura

```
explorando_dados_web/
├── requirements.txt
├── README.md
├── main.py
├── nivel1_basico.py
├── nivel2_intermediario.py
├── nivel3_avancado.py
└── utils.py
```