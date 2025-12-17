def bmi_calculator():
    """
    Formula: BMI = Weight (kg) / height (m)^2
    """
    print("\n--- BMI Category Determination ---")

    try: 
        height = float(input("Enter your height in meters (e.g. 1.75): "))
        weight = float(input("Enter your weight in kilograms (e.g. 70): "))

        if height <= 0 or weight <= 0:
            print("Error : HEight and weight must be positive values.")
            return 
        bmi = weight/(height ** 2)

        print(f"\n Calculated BMI: {bmi:.2f}")

        #BMI Category using if-elif-else condition 

        if bmi >= 30 :
            category = "Obesity"
        elif bmi >= 25 : 
            catergory = "Overweight"
        elif bmi >= 18.5 :
            category = "Normal"
        else:
            category = "Underweight"
        
        print(f"Output: \"{category}\"")
    except ValueError:
        print("Invalid input, Please enter numerical values for height and weight.")
    except ZeroDivisionError:
        print("Error: height cannot be zero.")

    print("-" * 50)    

City_data = { 
    "Autralia" : ["Sydney", "Melbourne", "Brisbane"],
    "UAE" : ["Dubai", "Abu Dhabi", "Sharjah"],
    "India" : ["Bhopal", "Delhi", "Indore"]
}

def get_country(city):
    """helper function to find country of given city"""
    city_normalized = city.strip().title()
    for country, cities in City_data.items():
        if city_normalized in cities:
            return country
    return None

def determine_city_country():
    """ asks for one city and prints the country it belongs to"""
    print("\n City to COuntry FInder")

    city_name_input = input("Enter a city name:")
    country = get_country(city_name_input)
    if country:
        print(f"\"{city_name_input.strip().title()} is in {country}.\"")
    else:
        print(f"\"{city_name_input.strip().title()} not found in the database.\"")

    print("-" * 50)

def check_same_country():
    """ asks the user for name of two city to determine if they are in same country or not"""
    print("\n Check if two city are in same country or not")

    city1_input = input("Enter the first city : ")
    city2_input = input("Enter the Second city : ")

    country1 = get_country(city1_input)
    country2 = get_country(city2_input)

    city1_name = city1_input.strip().title()
    city2_name = city2_input.strip().title()

    print("\n output : ")

    if country1 is None or country2 is None:
        if country1 is None:
            print(f"\"{city1_name} not found in the database.\"")
        if country2 is None:
            print(f"\"{city2_name} not found in the database.\"")
        print("They Don't Belong to the same country ")
        
    elif country1 == country2:
        print(f"\"{city1_name} and {city2_name} both are in {country1}.\"")
    else:
        print(f"\"{city1_name} is in {country1} and {city2_name} is in {country2}.\"")
        print("They Don't Belong to the same country ")
    
    print("-" * 50)


if __name__ == "__main__":
    bmi_calculator()
    determine_city_country()
    check_same_country()