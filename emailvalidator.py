from validate_email import validate_email
from flask import Flask, render_template, request,jsonify, Response, json
import json

app = Flask(__name__)


@app.route('/search', methods=['POST'])
def search():
    searchTearm = request.form['searchbox']

    is_valid = validate_email(searchTearm,verify=True)
    return str(is_valid)

if __name__ == '__main__':
   app.run(debug = True)