# generators/soil_generator.py

import random

SOIL_TYPES = [
    "infértil",
    "quase fértil",
    "fértil"
]

def generate_soil_data():

    soil_type = random.choice(SOIL_TYPES)

    if soil_type == "infértil":

        return {
            "estádo do solo": soil_type,
            "ph": round(random.uniform(4.0, 5.5), 2),
            "nitrogênio": random.randint(5, 20),
            "fósforo": random.randint(5, 20),
            "potássio": random.randint(5, 20),
            "matéria_orgânica": round(random.uniform(0.5, 2.0), 2),
            "humidade": random.randint(10, 40),
            "temperatura": random.randint(20, 35)
        }

    elif soil_type == "quase fértil":

        return {
            "estádo do solo": soil_type,
            "ph": round(random.uniform(5.5, 6.2), 2),
            "nitrogênio": random.randint(20, 40),
            "fósforo": random.randint(20, 35),
            "potássio": random.randint(20, 35),
            "matéria_orgânica": round(random.uniform(2.0, 3.5), 2),
            "humidade": random.randint(30, 60),
            "temperatura": random.randint(18, 30)
        }

    else:

        return {
            "estádo do solo": soil_type,
            "ph": round(random.uniform(6.0, 7.0), 2),
            "nitrogênio": random.randint(40, 80),
            "fósforo": random.randint(40, 80),
            "potássio": random.randint(40, 80),
            "matéria_orgânica": round(random.uniform(3.0, 6.0), 2),
            "humidade": random.randint(40, 80),
            "temperatura": random.randint(15, 28)
        }
    return {
        "ph": round(random.uniform(4.0, 8.0), 2),

        "nitrogen": random.randint(5, 80),

        "phosphorus": random.randint(5, 80),

        "potassium": random.randint(5, 80),

        "organic_matter": round(
            random.uniform(0.5, 6.0),
            2
        ),

        "humidity": random.randint(10, 90),

        "temperature": random.randint(-10, 40)
    }