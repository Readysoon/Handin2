from flask import Flask, redirect, url_for, render_template
from random import randint

app = Flask(__name__)

cookies_data = {
  'mercury' : {'name': 'Mercury', 'link': 'mercury.html'},
  'venus' : {'name': 'Venus', 'link': 'venus.html'},
  'earth' : {'name': 'Earth', 'link': 'earth.html'},
}

@app.route('/')
def cookies():
  return render_template('planets.html', cookies=cookies_data)

app.run()