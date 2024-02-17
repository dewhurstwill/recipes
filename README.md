# recipes
## Credit to https://www.themealdb.com/ for making a good API for food recipes

# Why I have created this application

I have two goals this year:

* Trying new food recipes
* Eating healthier food

While there are books and applications I could use I wanted to give myself a good way to relearn python.

# Setting up the python application

## Make sure you have python3.10+ and pip installed and set up

1.) Clone the repo:
```
git clone https://github.com/scottieyarn1135/recipes.git
```
2.) run the following commands to install the packages required for the application to work:
```
cd recipes
pip install -r requirements.txt
```
3.) Check to see if the application works:
```
Python3 main.py --help
```
# You can run the following commands

```
python3 main.py food-category --> This will list the food category's that are available.

python3 main.py food-category-recipes beef --> This will show the beef recipe names this can be done for all the category's the category's are all one word for example chicken,seafood,vegan,beef,breakfast

python3 main.py recipes --> You will be asked what recipe you want to see -> Once you put the name in it should show you how to make it and it should show you a youtube link if available.
```
# My workflow with the app

This is how I use the applicaiton I will use Chicken as the example:

```
python3 main.py food-category

python3 main.py food-category-recipes chicken

Python3 main.py recipes
what recipe do you want:Teriyaki Chicken Casserole

Recipe is shown 👏
```
