import json
from operator import methodcaller

class Recipes:
    JSON_FILE = "data.json"

    @classmethod
    def load_file(cls):
        # open JSON file
        with open(cls.JSON_FILE, "r") as file:
            # return json object from file
            return json.load(file).get("recipes", [])

    @classmethod
    def get_by_name(cls, name: str):
        all_recipes = cls.load_file()
        for recipe in all_recipes:
            if recipe['name'] == name:
                return recipe

    @classmethod
    def update_recipe(cls, existing_recipe: dict, updated_recipe: dict):
        for key, value in existing_recipe.items():
            existing_recipe[key] = value



