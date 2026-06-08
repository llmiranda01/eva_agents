# agents/crop_agent.py

from google.adk.agents import LlmAgent

crop_agent = LlmAgent(
    name="crop_agent",
    model="gemini-3.5-flash",
    instruction="""
Você é um agrônomo especialista.

Analise os parâmetros finais do solo.

Determine quais culturas possuem
maior probabilidade de sucesso.

Retorne SOMENTE JSON.

Formato:

{
  "culturas_recomendadas": []
}
"""
)