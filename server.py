import os
import json
import helpers
from flask import flash, Flask, jsonify, redirect, render_template, request
from recipes import Recipes

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def return_recipe_names():
    # load all recipes
    all_recipes = Recipes.load_file()
    """PART 3 - POST route to add additional recipes to data.json"""
    if request.method == "POST":
        # get new recipe
        new_recipe = request.get_json()
        new_recipe_name = new_recipe['name']

        for recipe in all_recipes:
            # if recipe already in recipes, return error
            if recipe['name'] == new_recipe_name:
                return {'error: recipe exists'}
            else:
                all_recipes.append(new_recipe)
                Recipes.write(all_recipes)
    #PART 1 - GET route that returns all recipe names
    else:
        # get list of all recipe names
        recipe_names = [recipe['name'] for recipe in all_recipes]
        return jsonify({"recipeNames": recipe_names})

@app.route("/<recipe>")
def return_recipe_ingredients_and_num_steps(recipe):
    """PART 2 - GET route that takes in recipe name as a string and returns ingredients and # of steps"""
    recipe_obj = Recipes.get_by_name(recipe)
    if recipe_obj:
        result = {"details": {"ingredients": recipe_obj['ingredients'], "numSteps": len(recipe_obj['instructions'])}}
        return jsonify(result)
    return jsonify({})

@app.route('/update/<recipe>', methods=['GET', 'PATCH'])
def update_existing_recipe(recipe):
    """PART 4 - PUT route to update existing records"""
    if request.method == 'PATCH':
        all_recipes = Recipes.load_file()
        updated_recipe = request.get_json()
        recipe_name = updated_recipe['name']
        for existing_recipe in all_recipes:
            if existing_recipe['name'] == recipe_name:
                Recipes.update_recipe(existing_recipe, updated_recipe)
                Recipes.write(all_recipes)
                return "", 204
        return "Not found", 400
    return redirect('/')

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),debug=True),
    port=int(os.getenv('PORT', 4444))