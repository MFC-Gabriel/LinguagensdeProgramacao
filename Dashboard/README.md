# Dashboard de Vendas — Guia de Publicação (Fase 4)

Este projeto contém:

| Arquivo              | Função                                                          |
|-----------------------|------------------------------------------------------------------|
| `meu_dashboard.py`    | Código do dashboard (Fases 1, 2 e 3)                             |
| `vendas.csv`          | Base de dados de vendas (fictícia, gerada para o exercício)      |
| `requirements.txt`    | Lista de bibliotecas necessárias para rodar o app                |
| `gerar_dados.py`      | Script usado apenas para gerar o `vendas.csv` (não sobe pro app) |

## Rodando localmente (antes de publicar)

```bash
pip install -r requirements.txt
streamlit run meu_dashboard.py
```

O terminal mostrará um link (geralmente `http://localhost:8501`) — abra no navegador.

## Fase 4 — Publicando na nuvem gratuitamente

### 1. Versionamento (GitHub)
1. Crie uma conta no [GitHub](https://github.com) se ainda não tiver.
2. Crie um **novo repositório** (pode ser público), ex.: `dashboard-vendas`.
3. Faça upload (ou `git push`) destes dois arquivos **na raiz do repositório**:
   - `meu_dashboard.py`
   - `vendas.csv`
   - `requirements.txt`

   Via linha de comando, dentro da pasta do projeto:
   ```bash
   git init
   git add meu_dashboard.py vendas.csv requirements.txt
   git commit -m "Dashboard de vendas - versão inicial"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/dashboard-vendas.git
   git push -u origin main
   ```

### 2. Dependências
Já está pronto: o `requirements.txt` gerado contém `streamlit` e `pandas`, que são exatamente as bibliotecas importadas no script.

### 3. Streamlit Community Cloud
1. Acesse **https://share.streamlit.io** (Streamlit Community Cloud).
2. Clique em **"Sign in"** e entre com sua conta do GitHub, autorizando o acesso.

### 4. Deploy
1. Clique em **"New app"**.
2. Selecione:
   - **Repository**: `SEU_USUARIO/dashboard-vendas`
   - **Branch**: `main`
   - **Main file path**: `meu_dashboard.py`
3. Clique em **"Deploy"**.
4. Em poucos minutos, a plataforma instala as dependências do `requirements.txt` e gera um link público, algo como:
   `https://dashboard-vendas-seuusuario.streamlit.app`

Pronto — esse link pode ser compartilhado com qualquer pessoa (ex.: o gestor/tomador de decisão), sem precisar configurar servidor algum.

> **Dica:** sempre que você alterar `meu_dashboard.py` no GitHub (novo commit/push), o Streamlit Community Cloud atualiza o app publicado automaticamente.
