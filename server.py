from flask import Flask
from scrape import scrape

app = Flask(__name__)

@app.route("/")
def defaultData(country='india'):
    return scrape(country)

@app.route("/<country>")
def fetchdata(country='india'):
    return scrape(country)
