from numpy.random import choice, randint
import time
import json
from flask import Flask

def get_random_value():
    new_dict = {}

    city_list = ['New York', 'Los Angeles', 'Chicago',
                 'Houston', 'Philadelphia', 'Moscow',
                 'London', 'Santiago', 'Paris']

    currency_list = ['RUB', 'USD', 'EUR', 'GBP']

    new_dict['branch'] = choice(city_list)
    new_dict['currency'] = choice(currency_list)
    new_dict['amount'] = randint(-100, 100)

    return new_dict

# while True:
#     data = get_random_value()
#     time.sleep(1)
#     json_object = json.dumps(data, indent = 4)
#     print(json_object)

app = Flask(__name__)

@app.route("/")
def dataSender():
    data = get_random_value()
    return data


@app.route('/healthz')
def healthz():
    return "OK"

@app.route('/healthx')
def healthx():
    time.sleep(1)
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0')