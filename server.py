from flask import Flask
from scrape import scrape

app = Flask(__name__)

@app.route("/<country>")
def fetchdata(country='india'):
    return scrape(country)
