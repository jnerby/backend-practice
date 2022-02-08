import os
import helpers
from flask import flash, Flask, jsonify, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def return_all_recipes():
    """PART 1 - GET route that returns all recipe names"""
    all_recipes = helpers.get_all_recipes() 
    return jsonify(all_recipes)

"""PART 2 - GET route that takes in recipe name as a string and returns ingredients and # of steps"""
"""PART 3 - POST route to add additional recipes to data.json"""
"""PART 4 - PUT route to update existing records"""

if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0')),
    port=int(os.getenv('PORT', 4444))