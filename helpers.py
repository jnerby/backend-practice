import json

from sqlalchemy import all_

def load_json():
    """Returns data from data.json"""
    with open('data.json', 'r') as f:
        all_recipes = json.load(f).get('recipes', [])

    return all_recipes

def get_all_recipe_names():
    """Returns all recipes from data.json"""
    all_recipes = load_json()
    all_recipe_names = [recipe.get("name") for recipe in all_recipes]
   
    return all_recipe_names

def get_recipe_by_name(recipe_name):
    all_recipes = load_json()
    for recipe in all_recipes:
        if recipe['name'] == recipe_name:
            return recipe
        else:
            return 'Not found'

def get_ingredients(recipe_name):
    if recipe_name:
        recipe = get_recipe_by_name(recipe_name)
        return recipe['ingredients']

def get_num_steps(recipe_name):
    if recipe_name:
        recipe = get_recipe_by_name(recipe_name)
        return len(recipe['instructions'])
