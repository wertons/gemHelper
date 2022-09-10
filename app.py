from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__)
app.config.from_object(__name__)

DEBUG = True
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def home():
    return "Hewwo"

@app.route("/gemList", methods=['POST'])
def main():
    from gemList import getProfitPerGem
    options = request.get_json()["options"]
    return getProfitPerGem(
        options["corruptedCheck"],
        options["awakenedCheck"],
        options["altQualCheck"],
        options["qualityCheck"]
    )
