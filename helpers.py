import json

def get_all_recipes():
    """Returns all recipes from data.json"""
    ## how to access data from a .json
    with open('data.json', 'r') as f:
        all_recipes = json.load(f)
    return all_recipes