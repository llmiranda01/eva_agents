from agents.soil_agent import SoilAgent

soil = {
    "ph": 5.2,
    "nitrogênio": 12,
    "fósforo": 8,
    "potássio": 18,
    "matéria_orgânica": 1.5
}

agent = SoilAgent()

result = agent.analyze(soil)

print(result)