from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(_name_)

mongo = PyMongo(app, url= 'mongodb://localhost:27017/mars_db')

@app.route('/')
def home():
    mars_data = mongo.db.facts.find_one()
    return render_template('index.html', mars_data=mars_data)

@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()

    mongo.db.facts.update({}, mars_data, upsert=True)

    return redirect('/')

if__name__ == '__main__':
    app.run(debug=True)