from flask import Flask , render_template, jsonify, request

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/greeting')
def greeting():
    owner = "Akilah"
    return render_template('index.html', owner=owner)

 #global variable
 ingredients = ['Apple', 'Eggs', 'Flour']   

@app.route('/pie')
def pie():
    # recipes = {
    #     'pie ingredients': ['apples', 'sugar', 'flour']
    #     }
    # return jsonify({'pie ingredients': recipes['pie ingredients'][0]})

    # ANNAS CODEALONG VVVV
    if request.method == 'POST':
        global ingredients

        ingredients = request.form['ingredients']
        ingredients.append(ingredient)
        print(ingredients)
        #shows random ingredient once user has inputted an new ingredient in form
        index = random.randint(0, (len(ingredients)-1))

        return jsonify({'pie ingredient': ingredients[index]})

    else:
        return render_template('pieForm.html')



