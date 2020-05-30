import time
import random

from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
PrometheusMetrics(app)


endpoints = ('ep_one', 'ep_two', 'ep_three', 'ep_four', 'error')


@app.route('/ep_one')
def first_route():
    time.sleep(random.random() * 0.2)
    return '1'


@app.route('/ep_two')
def the_second():
    time.sleep(random.random() * 0.4)
    return '2'


@app.route('/ep_three')
def test_3rd():
    time.sleep(random.random() * 0.6)
    return '3'


@app.route('/ep_four')
def fourth_one():
    time.sleep(random.random() * 0.8)
    return '4'


@app.route('/error')
def oops():
    return 'error', 500


if __name__ == '__main__':
    app.run('0.0.0.0', 5000, threaded=True)
