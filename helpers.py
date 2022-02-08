import json

def get_all_recipe_names():
    """Returns all recipes from data.json"""
    with open('data.json', 'r') as f:
        all_recipes = json.load(f)
        all_recipe_names = [recipe['name'] for recipe in all_recipes['recipes']]
   
    return all_recipe_names