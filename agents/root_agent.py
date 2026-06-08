# agents/root_agent.py

from google.adk.agents import LlmAgent

from agents.soil_agent import soil_agent
from agents.fungus_agent import fungus_agent
from agents.crop_agent import crop_agent

root_agent = LlmAgent(
    name="root_agent",
    model="gemini-3.5-flash",
    description="Coordenador do sistema",

    sub_agents=[
        soil_agent,
        fungus_agent,
        crop_agent
    ],

    instruction="""
Coordene os agentes.

1. Solo
2. Fungo
3. Culturas

Sempre encaminhe para o agente mais adequado.
"""
)