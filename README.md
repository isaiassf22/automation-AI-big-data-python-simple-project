# Automation + AI + Big Data (Python) — projetos simples

Repositório com experimentos em Python feitos para praticar:
- **Geração de PDF**
- **Automação de tarefas** (PyAutoGUI)
- **Coleta de dados financeiros** (yfinance)
- **Análise de dados (Big Data) com Pandas** usando uma planilha com ~70.000 linhas (`vendas.xlsx`)

> Observação: este repo é uma coleção de scripts curtos (estilo laboratório). A intenção é demonstrar fundamentos e prática com bibliotecas populares.

---

## Estrutura

- `first.py`  
  Gera um PDF simples usando `fpdf`.

- `atomationProject.py`  
  Automação de navegação/ações no navegador usando `pyautogui` + `pyperclip`.  
  ⚠️ Usa coordenadas fixas de tela (x,y).

- `firstAI.py`  
  Coleta dados de um ativo via `yfinance` e imprime as primeiras linhas (ex.: PETR4.SA).

- `firstBigData.py`  
  Lê a base `vendas.xlsx` (70.000 linhas) e calcula estatísticas/contagens com pandas.

Arquivos auxiliares:
- `vendas.xlsx` (base de dados)
- `testing.pdf` / `testing2.pdf` (arquivos de teste)

---

## Requisitos

- Python 3.10+ (recomendado)
- Bibliotecas:
  - `pandas`
  - `openpyxl` (para ler `.xlsx`)
  - `fpdf`
  - `yfinance`
  - `pyautogui`
  - `pyperclip`

---

## Como rodar

### 1) Criar e ativar ambiente virtual
**Windows (PowerShell)**
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1

