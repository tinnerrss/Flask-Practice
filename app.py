from flask import Flask, render_template, jsonify, request
import random

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'


@app.route('/greeting')
def greeting():
    return render_template('index.html', name="Akilah")


 # create initial list of ingredients
ingredients = ["Flour", "Butter", "Apples"]

@app.route('/pie', methods=['GET', 'POST'])
def pie():
    global ingredients
    if request.method == 'POST':
        # get user input for ingredient and append to ingredients
        ingredient = request.form["ingredient"]
        ingredients.append(ingredient)

        # get a random number between 0-length of list and set to index
        index = random.randint(0, (len(ingredients) - 1))
    
        # return a json object with random pie ingredient
        return jsonify({'pie ingredient': ingredients[index]})
    else:
        return render_template('pieForm.html')
