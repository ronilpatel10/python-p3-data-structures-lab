spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of foods with a heat_level over 5.

    Parameters:
    - spicy_foods (list of dicts): A list of dictionaries representing spicy foods.

    Returns:
    - list: A list of dictionaries representing spiciest foods.
    """
    return [food for food in spicy_foods if food.get("heat_level", 0) is not None and food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    """
    Prints each spicy food in the specified format.

    Parameters:
    - spicy_foods (list of dicts): A list of dictionaries representing spicy foods.
    """
    for food in spicy_foods:
        name = food.get("name", "Unknown")
        cuisine = food.get("cuisine", "Unknown")
        heat_level = food.get("heat_level", 0)

        print(f"{name} ({cuisine}) | Heat Level: {'🌶' * heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns a single dictionary representing the spicy food whose cuisine matches the provided cuisine.

    Parameters:
    - spicy_foods (list of dicts): A list of dictionaries representing spicy foods.
    - cuisine (str): The cuisine to match.

    Returns:
    - dict or None: A dictionary representing the matching spicy food, or None if not found.
    """
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
    return None


def print_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get("heat_level", 0) > 5]

    for food in spiciest_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")


def get_average_heat_level(spicy_foods):
    """
    Returns an integer representing the average heat level of all the spicy foods.

    Parameters:
    - spicy_foods (list of dicts): A list of dictionaries representing spicy foods.

    Returns:
    - int: The average heat level.
    """
    total_heat = sum(food.get("heat_level", 0) for food in spicy_foods)
    num_spicy_foods = len(spicy_foods)

    if num_spicy_foods > 0:
        return total_heat // num_spicy_foods
    else:
        return 0

def create_spicy_food(spicy_foods, spicy_food):
    """
    Adds a new spicy food to the list of spicy foods.

    Parameters:
    - spicy_foods (list of dicts): A list of dictionaries representing spicy foods.
    - spicy_food (dict): A dictionary representing the new spicy food to be added.

    Returns:
    - list: The updated list of spicy foods.
    """
    spicy_foods.append(spicy_food)
    return spicy_foods
