# agents/soil_agent.py

from google.adk.agents import LlmAgent

soil_agent = LlmAgent(
    name="soil_agent",
    model="gemini-3.5-flash",
    instruction="""
Você é um especialista em ciência do solo.

Analise os dados recebidos.

Classifique o solo em:

- infertil
- quase_fertil
- fertil

Regras:

fertil:
- todos os parâmetros adequados

quase_fertil:
- apenas 1 ou 2 problemas leves

infertil:
- múltiplos problemas ou problemas graves

Retorne APENAS JSON.

Formato obrigatório:

{
  "status_solo": "",
  "score_fertilidade": 0,
  "problemas": [],
  "recomendacoes": []
}
"""
)