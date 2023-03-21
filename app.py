from flask import Flask, redirect, url_for, render_template
from random import randint

app = Flask(__name__)

planets_data = {
  'mercury' : {'name': 'Mercury', 'link': 'mercury.html'},
  'venus' : {'name': 'Venus', 'link': 'venus.html'},
  'earth' : {'name': 'Earth', 'link': 'earth.html'},
}

@app.route('/')
def planets():
  return render_template('planets.html', planets = planets_data)

@app.route('/<slug>')
def slugplanets(slug):
  return render_template(f"{slug}.html", name = planets_data[slug]['name'], pic = f"{slug}.jpg", planets = planets_data)

app.run()