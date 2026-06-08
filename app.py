from fastapi import FastAPI
from agents.soil_agent import SoilAgent
from agents.fungus_agent import FungusAgent

from generators.soil_generator import (
    generate_soil_data
)

from agents.soil_agent import (
    SoilAgent
)

app = FastAPI()

soil_agent = SoilAgent()

@app.get("/")
def home():
    return {
        "message": "Smart Soil API"
    }



@app.get("/soil")
def get_soil():
    return generate_soil_data()

@app.get("/analyze")
def analyze_soil():

    soil_data = generate_soil_data()

    analysis = soil_agent.analyze(
        soil_data
    )

    return {
        "soil_data": soil_data,
        "analysis": analysis
    }

soil_agent = SoilAgent()
fungus_agent = FungusAgent()

@app.get("/analyze/full")
def analyze_full():

    soil_data = generate_soil_data()

    print(soil_data)

    soil_analysis = soil_agent.analyze(
        soil_data
    )

    fungus_strategy = (
        fungus_agent.create_strategy(
            soil_analysis
        )
    )

    return {
        "dados_solo": soil_data,
        "analise_solo": soil_analysis,
        "estrategia_fungo": fungus_strategy
    }