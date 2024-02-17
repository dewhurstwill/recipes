import typer
import requests 
from rich import print

app = typer.Typer()
food_url_categories=requests.get("https://www.themealdb.com/api/json/v1/1/categories.php").json()
food_url_menu=requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=").json()

@app.command()
def food_category():
    for menulist in food_url_categories["categories"]:
        categoryName = menulist['strCategory']
        categoryDescription = menulist['strCategoryDescription']
        categoryImage = menulist['strCategoryThumb']
        print(f'\n{categoryName}\n')
        print(f'Image of URL found here: {categoryImage}')
        print(f'\n{categoryDescription}')
@app.command()
def food_category_recipes(category : str): 
    match category:
        case "1" | "Beef" | "beef":
            food_category = "Beef"
        case "2" | "Chicken" | "chicken":
            food_category = "Chicken"
        case "3" | "Dessert" | "dessert":
            food_category = "Dessert"
        case "4" | "Lamb" | "lamb":
            food_category = "Lamb"
        case "5" | "Miscellaneous" | "miscellaneous":
            food_category = "Miscellaneous"
        case "6" | "Pasta" | "pasta":
            food_category = "Pasta"
        case "7" | "Pork" | "pork":
            food_category = "Pork"
        case "8" | "Seafood" | "seafood":
            food_category = "Seafood"
        case "9" | "Side" | "side":
            food_category = "Side"
        case "10" | "Starter" | "starter":
            food_category = "Starter"
        case "11" | "Vegan" | "vegan":
            food_category = "Vegan"
        case "12" | "Vegetarian" | "vegetarian":
            food_category = "Vegetarian"
        case "13" | "Breakfast" | "breakfast":
            food_category = "Breakfast"
        case "14" | "Goat" | "goat":
            food_category = "Goat"

    food_category_recipes_base_url = f'https://www.themealdb.com/api/json/v1/1/filter.php?c='
    food_menu_full_url = food_category_recipes_base_url + food_category
    food_menu_response = requests.get(food_menu_full_url).json()
    for food_items in food_menu_response['meals']:
        title = food_items['strMeal']
        picture = food_items['strMealThumb']
        print(f'\nFood Name : {title}\n')
        print(f'\nLink to a picture of the food : {picture}\n')

@app.command()
def recipes():
    name = input("What Recipe do you want? :")
    recipes_base_url = f'https://www.themealdb.com/api/json/v1/1/search.php?s='
    recipes_full_url = f'{recipes_base_url}{name}'
    recipes_response = requests.get(recipes_full_url).json()['meals'][0]
    title = recipes_response['strMeal']
    location = recipes_response['strArea']
    instructions = recipes_response['strInstructions']
    image = recipes_response['strMealThumb']
    youtube = recipes_response['strYoutube']
    ingredient1 = recipes_response['strIngredient1']
    ingredient2 = recipes_response['strIngredient2']
    ingredient3 = recipes_response['strIngredient3']
    ingredient4 = recipes_response['strIngredient4']
    ingredient5 = recipes_response['strIngredient5']
    ingredient6 = recipes_response['strIngredient6']
    ingredient7 = recipes_response['strIngredient7']
    ingredient8 = recipes_response['strIngredient8']
    ingredient9 = recipes_response['strIngredient9']
    ingredient10 = recipes_response['strIngredient10']
    ingredient11 = recipes_response['strIngredient11']
    ingredient12 = recipes_response['strIngredient12']
    ingredient13 = recipes_response['strIngredient13']
    ingredient14 = recipes_response['strIngredient14']
    ingredient15 = recipes_response['strIngredient15']
    measure1     = recipes_response['strMeasure1']
    measure2     = recipes_response['strMeasure2']
    measure3     = recipes_response['strMeasure3']
    measure4     = recipes_response['strMeasure4']
    measure5     = recipes_response['strMeasure5']
    measure6     = recipes_response['strMeasure6']
    measure7     = recipes_response['strMeasure7']
    measure8     = recipes_response['strMeasure8']
    measure9     = recipes_response['strMeasure9']
    measure10    = recipes_response['strMeasure10']
    measure11    = recipes_response['strMeasure11']
    measure12    = recipes_response['strMeasure12']
    measure13    = recipes_response['strMeasure13']
    measure14    = recipes_response['strMeasure14']
    measure15    = recipes_response['strMeasure15']

    print(f'\n Recipes Name : {title}\n')
    print(f'\n Where is the Recipe from : {location}\n')
    print(f'\n URL for Image : {image}\n')
    print(f' Ingredient 1 : {ingredient1} : {measure1}')
    print(f' Ingredient 2 : {ingredient2} : {measure2}')
    print(f' Ingredient 3 : {ingredient3} : {measure3}')
    print(f' Ingredient 4 : {ingredient4} : {measure4}')
    print(f' Ingredient 5 : {ingredient5} : {measure5}')
    print(f' Ingredient 6 : {ingredient6} : {measure6}')
    print(f' Ingredient 7 : {ingredient7} : {measure7}')
    print(f' Ingredient 8 : {ingredient8} : {measure8}')
    print(f' Ingredient 9 : {ingredient9} : {measure9}')
    print(f' Ingredient 10 : {ingredient10} : {measure10}')
    print(f' Ingredient 11 : {ingredient11} : {measure11}')
    print(f' Ingredient 12 : {ingredient12} : {measure12}')
    print(f' Ingredient 13 : {ingredient13} : {measure13}')
    print(f' Ingredient 14 : {ingredient14} : {measure14}')
    print(f' Ingredient 15 : {ingredient15} : {measure15}')
    print(f'\n Link to youtube video : {youtube}\n')
    print(f'\n Instructions : {instructions}\n')
    
if __name__ == "__main__":
    app()
