# main.py
from tracker import start_tracking

def main():
    print("Welcome to the Python Fitness Tracker App!")
    choice = input("Start tracking? (yes/no): ").strip().lower()

    if choice == "yes":
        duration = input("Enter duration in seconds (default 30): ").strip()
        interval = input("Enter interval in seconds (default 5): ").strip()

        # Default values if user enters nothing
        duration = int(duration) if duration else 30
        interval = int(interval) if interval else 5

        print(f"\nStarting tracking for {duration} seconds (update every {interval} sec)...")
        start_tracking(duration, interval)
        print("\nTracking complete. Stay fit!")

    else:
        print("Exiting the app. Stay healthy!")

if __name__ == "__main__":
    main()
