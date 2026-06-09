# Smart Soil AI

Sistema Multiagente para Análise Inteligente de Solos Utilizando Google ADK e Gemini

---

## Visão Geral

O Smart Soil AI é um sistema multiagente desenvolvido para analisar a qualidade do solo e gerar estratégias de recuperação utilizando Inteligência Artificial.

O projeto simula sensores agrícolas e utiliza agentes especializados construídos com o Google Agent Development Kit (ADK) e modelos Gemini para interpretar dados do solo, propor ações biológicas e recomendar culturas adequadas.

---

## Problema

A análise de solo normalmente exige conhecimento técnico especializado e interpretação manual de diversos parâmetros químicos e físicos.

O Smart Soil AI busca automatizar parte desse processo através de agentes de IA que:

- Avaliam a fertilidade do solo;
- Identificam problemas nutricionais;
- Propõem estratégias de recuperação utilizando fungos;
- Recomendarão culturas adequadas para plantio.

---

## Arquitetura

```text
Sensor IoT (Simulado)
        │
        ▼
+----------------+
|   SoilAgent    |
+----------------+
        │
        ▼
+----------------+
|  FungusAgent   |
+----------------+
        │
        ▼
+----------------+
|   CropAgent    |
+----------------+
        │
        ▼
Recomendação Final
```

---

## Agentes

### SoilAgent

Responsável por analisar os dados recebidos dos sensores.

Avalia:

- pH
- Nitrogênio
- Fósforo
- Potássio
- Matéria Orgânica

Classifica o solo como:

- fértil
- quase_fértil
- infértil

#### Exemplo

```json
{
  "status_solo": "infertil",
  "score_fertilidade": 25,
  "problemas": [
    "ph_baixo",
    "nitrogenio_baixo"
  ]
}
```

---

### FungusAgent

Responsável por criar estratégias de recuperação do solo utilizando princípios inspirados em comunicação fúngica.

Recebe:

```json
{
  "problemas": [...]
}
```

Retorna:

```json
{
  "intensidade": "alta",
  "plano_acao_fungo": [...]
}
```

---

### CropAgent

> Em desenvolvimento

Será responsável por recomendar culturas agrícolas adequadas para o estado atual do solo.

Exemplos:

- Alface
- Tomate
- Feijão
- Milho
- Cenoura

---

## Tecnologias Utilizadas

### Backend

- Python 3.14
- FastAPI
- Uvicorn

### Inteligência Artificial

- Google ADK 2.2.0
- Gemini 2.5 Flash

### Utilidades

- Python Dotenv
- AsyncIO

---

## Estrutura do Projeto

```text
smart-soil/
│
├── app.py
│
├── agents/
│   ├── soil_agent.py
│   ├── fungus_agent.py
│   ├── crop_agent.py
│   └── root_agent.py
│
├── generators/
│   └── soil_generator.py
│
├── test_adk.py
│
├── .env
│
└── README.md
```

---

## Instalação

### 1. Clonar o projeto

```bash
git clone <repositorio>
cd smart-soil
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

#### Git Bash

```bash
source venv/Scripts/activate
```

#### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```bash
pip install fastapi
pip install uvicorn
pip install google-adk
pip install google-genai
pip install python-dotenv
```

Ou:

```bash
pip install -r requirements.txt
```

---

## Configuração

Crie um arquivo chamado:

```text
.env
```

Adicione:

```env
GOOGLE_API_KEY=SUA_CHAVE_GEMINI
```

---

## Executando o Projeto

### Iniciar a API

```bash
uvicorn app:app --reload
```

Acesse:

```text
http://localhost:8000/docs
```

---

## Endpoints

### Home

```http
GET /
```

#### Resposta

```json
{
  "message": "Smart Soil API"
}
```

---

### Dados do Sensor

```http
GET /soil
```

Retorna um conjunto de dados de solo gerado aleatoriamente.

---

### Análise do Solo

```http
GET /analyze
```

Fluxo executado:

```text
Sensor
 ↓
SoilAgent
```

---

### Fluxo Completo

```http
GET /analyze/full
```

Fluxo executado:

```text
Sensor
 ↓
SoilAgent
 ↓
FungusAgent
```

#### Resposta

```json
{
  "dados_solo": {},
  "analise_solo": {},
  "estrategia_fungo": {}
}
```

---

## Testando os Agentes

Execute:

```bash
python test_adk.py
```

Fluxo executado:

```text
Sensor Simulado
      ↓
SoilAgent (Gemini)
      ↓
FungusAgent (Gemini)
```

---

## Exemplo de Resultado

```json
{
  "status_solo": "infertil",
  "score_fertilidade": 25,
  "problemas": [
    "ph_baixo",
    "nitrogenio_baixo",
    "fosforo_baixo"
  ],
  "recomendacoes": [
    "corrigir_ph",
    "adubacao_nitrogenada"
  ]
}
```

---

## Próximas Etapas

### CropAgent

Recomendação inteligente de culturas agrícolas.

### RootAgent

Coordenação automática dos agentes utilizando ADK.

### Banco de Dados

Persistência dos dados históricos do solo e das análises.

### RAG

Consulta de conhecimento agrícola especializado.

### Word2Vec

Representação semântica de nutrientes, fungos e culturas para enriquecer recomendações.

---

## Objetivos do Projeto

- Aprender sistemas multiagentes com Google ADK;
- Aplicar IA generativa ao agronegócio;
- Simular sensores agrícolas;
- Criar fluxos colaborativos entre agentes especializados;
- Evoluir para um sistema com memória, RAG e recomendação inteligente de culturas.

---

## Autor

Projeto desenvolvido para estudo de:

- Sistemas Multiagentes
- Google ADK
- Gemini
- Agricultura Inteligente
- Inteligência Artificial Aplicada ao Agronegócio

---

## Licença

Projeto acadêmico e experimental.

Uso livre para fins educacionais, pesquisa e aprendizado.
