### ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Python Programming: Flask

This assignment was adapted from this [homework](https://git.generalassemb.ly/python-programming/python-programming/tree/revisions_v2.1/unit-6-flask/instructor-resources/hw-5day-4flask) from [GA's Python Part-Time](https://generalassemb.ly/education/python-programming) course.

<!---
This assignment was originally developed by Kevin

Questions? Comments?
1. Log an issue to this repo to alert me of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Hit me up on Slack at @kevin.coyle.

Note: Adaptation made in fall 2019 by Brandi Butler.
--->

# Flask: Practice Problems

In this homework, you're going to write code for a few problems.

You will practice these programming concepts we've covered in class:

* Rendering templates
* Passing variables to templates
* Creating an API
* Making `GET`/`POST` requests

------------

## Deliverables

For this assignment you will be creating ONE Flask app. Each problem listed below will direct you to create a route or feature within that app.

*Reminder: On your laptop, you can run your server from your command line with the following command:*

```
flask run
```

> **Hint**: After finish writing code for each problem, launch your server, go into your browser, and be sure that your Flask app is outputting the intended data.


## Requirements:

* By the end of this, you should have ONE Flask app that meets the following criteria:

| METHOD | PATH | FUNCTIONALITY |
| ------ | ------------- | ---------------------------------------------------------- |
| GET | `/` | Render a home page that sends the string "Hello World" |

------------

## Problem 1: Hello World

Set up a Flask app skeleton. This will include making a python server file - this will be named something like `app.py`. 

`app.py` should include the following:

* Import Flask
* Declare your app variable
* Make your home page route (Hint: Use `@app.route()`)
* Return the string "Hello World"

At this point, run your app with `flask run` and see what happens!

> HINT: You may want to set some environment variables such as FLASK_APP and FLASK_ENV.

If you ran into an error when running your app, try setting these variables via the command line:

```
export FLASK_ENV=development
export FLASK_APP=app.py
```

## Problem 2: "Rendering Like Rembrandt"

### Skill You're Practicing: Using templates to render Python.

Create a Flask app that renders an HTML template. In the template, display a greeting and a `name` variable (don't forget to pass the template the argument!).

Then, create a CSS change the color of the font of your template's variable.

#### Example Test Code

```
render_template('index.html', name=user)
```

#### Example Test Output
```
"Hi there Akilah. It's great to see you today!"
```

**Hint 1:**

Remember: Templates for variables use the double brackets `{{}}`.

**Hint 2:**

Don't forget the module `render_template`.

**Hint 3:**

Your directory should look like:

```
project
│   
│
└───app
│   │   problem1.py
│   │   
│   │
│   └───templates
│   │    └─── index.html
│   │
│   │
│   └───static
│       └───style.css
```

------

## Problem 2: "A Detective, a PI"

### Skill You're Practicing: Creating an API.

Write a Flask app that makes a `GET` request and returns a JSON of one of the items in a list.


#### Example Test Code
```
return jsonify({'pie ingredient': 'ingredients[0]'})
```

#### Example Test Output
```
{'pie ingredient': 'apples'}
```

**Hint 1:**

Refer to your class notes from the Variables lesson for how to read in a variable directly in a Flask app.

**Hint 2:**

There are two modules that we'll need to execute this, in addition to our standard `from flask import Flask`: `jsonify`, and `requests`.

**Hint 3:**

Try passing the variable name into your function, as well as making that your endpoint in the route.

----

## Problem 3: "The POST Man Deliverth"

### Skill You're Practicing: Creating an API.

Write a Flask app that makes a `POST` request and returns a JSON of one of the items in a list.


#### Example Test Code
```
ingredients.append(ingredient)
return jsonify({'pie ingredient': ingredients})
```

#### Example Test Output
```
{'pie ingredient': 'apples'}
```

**Hint 1:**

Refer to your class notes from the Variables lesson for how to read in a variable directly in a Flask app.

**Hint 2:**

There are two modules that we'll need to execute this, in addition to our standard `from flask import Flask`: `jsonify`, and `requests`.

**Hint 3:**

Try passing the variable name into your function, as well as making that your endpoint in the route.

**Hint 4:**

`request.get_json()`
