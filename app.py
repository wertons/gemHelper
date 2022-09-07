from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

DEBUG = True
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def home():
    return "Hewwo"

@app.route("/gemList", methods=['GET'])
def main():
    from gemList import getProfitPerGem
    return getProfitPerGem()
