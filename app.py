from flask import Flask
from flask import render_template, request, json, redirect, url_for
from requests import Request, Session
import json
import os

from requests import api

app = Flask(__name__)
apiKey = os.environ.get('APIKEY')

@app.route("/")
def index():
    # params = {
    #     'CMC_PRO_API_KEY': apiKey,
    #     'value': {'id': 1}
    # }

    # response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/info", params=params)
    # json_data = json.loads(response.text)
    # json_text = str(json_data['status'])

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'
    parameters = {
        'id':'1'
    }
    headers = {
        'X-CMC_PRO_API_KEY': apiKey,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)

    return render_template('index.html', t=data)

if __name__ == "__main__":
  app.run()