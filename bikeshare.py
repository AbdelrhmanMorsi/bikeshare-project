# Refactored version
def welcome_user():
    print("Welcome to the Refactored Bikeshare!")
    print("This script now handles input more robustly.")

def choose_city():
    cities = ["Chicago", "New York City", "Washington"]
    for idx, name in enumerate(cities, 1):
        print(f"{idx}. {name}")
    while True:
        try:
            sel = int(input("Select a city number (1-3): "))
            if 1 <= sel <= 3:
                return cities[sel-1]
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    welcome_user()
    city = choose_city()
    print(f"You chose {city}.")

if __name__ == "__main__":
    main()