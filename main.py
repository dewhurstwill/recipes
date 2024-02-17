import typer
import requests

app = typer.Typer()

@app.command()
def food_category():
    categories = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php").json()
    for category in categories["categories"]:
        print(f"\n{category['strCategory']}\nImage of URL found here: {category['strCategoryThumb']}\n{category['strCategoryDescription']}")

@app.command()
def food_category_recipes(category: str):
    categories = {
        "1": "Beef", "2": "Chicken", "3": "Dessert", "4": "Lamb",
        "5": "Miscellaneous", "6": "Pasta", "7": "Pork", "8": "Seafood",
        "9": "Side", "10": "Starter", "11": "Vegan", "12": "Vegetarian",
        "13": "Breakfast", "14": "Goat"
    }
    category = categories.get(category, category.capitalize())
    url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
    meals = requests.get(url).json()
    for meal in meals['meals']:
        print(f"\nFood Name: {meal['strMeal']}\nLink to a picture of the food: {meal['strMealThumb']}\n")

@app.command()
def recipes():
    name = input("What Recipe do you want? :")
    recipe = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}").json()['meals'][0]
    print(f"\nRecipes Name: {recipe['strMeal']}\nWhere is the Recipe from: {recipe['strArea']}\nURL for Image: {recipe['strMealThumb']}")
    for i in range(1, 16):
        ingredient = recipe[f'strIngredient{i}']
        measure = recipe[f'strMeasure{i}']
        if ingredient:  # Only print if ingredient is not empty
            print(f"Ingredient {i}: {ingredient}: {measure}")
    print(f"\nLink to youtube video: {recipe['strYoutube']}\n\nInstructions: {recipe['strInstructions']}\n")

if __name__ == "__main__":
    app()
