from flask import Flask , render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/greeting')
def greeting():
    owner = "Akilah"
    return render_template('index.html', owner=owner)

# @app.route('/pie')
# def pie():


