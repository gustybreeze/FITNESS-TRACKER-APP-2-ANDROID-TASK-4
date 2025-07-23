# data_generator.py
import random

def generate_mock_data():
    steps = random.randint(2000, 10000)
    distance_km = round(steps * 0.0008, 2)  # average step length
    calories = round(steps * 0.04, 2)       # estimated calories burned per step
    return {
        "steps": steps,
        "distance_km": distance_km,
        "calories": calories
    }
