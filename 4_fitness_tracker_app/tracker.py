# tracker.py
import time
from data_generator import generate_mock_data

def start_tracking(duration=30, interval=5):

    elapsed = 0
    while elapsed < duration:
        data = generate_mock_data()
        print(f"\nTime: {elapsed} sec")
        print(f"Steps: {data['steps']}")
        print(f"Distance: {data['distance_km']} km")
        print(f"Calories: {data['calories']} kcal")
        time.sleep(interval)
        elapsed += interval