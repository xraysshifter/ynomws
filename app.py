from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, DateField
import random
from data import *

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip

def randomchoice(l):
    return random.choice(l)

app.jinja_env.filters['randomchoice'] = randomchoice


def add_price_to_name():
    m = []
    with open('names.txt', 'r') as file:
        names = [name.rstrip() for name in file]
    for name in names:
        price = round(random.uniform(100.0, 2500.5),2)
        name_n_price_list = [name, price]
        m.append(name_n_price_list)    

    return m

@app.route('/')
def index():
    gwords = [word for word in prefix_list]
    print(gwords)
    m = add_price_to_name()
    names = [row[0] for row in m]
    paid = [row[1] for row in m]
    print(names, '\++++/', paid)
    
    return render_template('index.html', names=names, paid=paid, gwords=gwords, zip=zip, randomchoice=randomchoice)

if __name__ == '__main__':
    app.run(debug=True)

