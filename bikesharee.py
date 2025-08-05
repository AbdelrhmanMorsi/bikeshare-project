# bikeshare.py
# Author: Abderhman Morsi 
# Bikeshare project main code

def welcome():
    print("Welcome to Bikeshare Refactored!")
    print("Let's get started.")

def get_city():
    cities = ["Chicago", "New York City", "Washington"]
    for idx, city in enumerate(cities, 1):
        print(f"{idx}. {city}")
    while True:
        try:
            choice = int(input("Choose a city (1-3): "))
            if 1 <= choice <= 3:
                return cities[choice - 1]
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a number.")

def main():
    welcome()
    city = get_city()
    print(f"You selected {city}.")

if __name__ == "__main__":
    main()