import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import quandl
from appenv import QUANDL_API_KEY

quandl.ApiConfig.api_key = QUANDL_API_KEY

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    symbol = request.values.get('Body')
    path = 'https://www.quandl.com/api/v3/datasets/WIKI/{0}.json'
    path = path.format(symbol)
    print(path)

    response = MessagingResponse()
    try:
        result = requests.get(path)
        print(result)
        price = result.json()['dataset']['data'][0][4]
        print(price)
        response.message('Current price of {0} is: {1}'.format(symbol, price))
    except:
        response.message('Could not find the symbol, please try again.')
    # response.message("Hello World")
    return str(response)

if __name__ == "__main__":
    app.debug = True
    app.run()

