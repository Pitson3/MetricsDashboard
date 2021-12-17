from flask import Flask, render_template, request, jsonify

import pymongo
from flask_pymongo import PyMongo

import logging
from jaeger_client import Config
from prometheus_flask_exporter import PrometheusMetrics

import os


app = Flask(__name__)
metrics = PrometheusMetrics(app)

#static information as metric. Adapted from https://github.com/rycus86/prometheus_flask_exporter/blob/master/examples/sample-signals/app/app.py
metrics.info('app_info', 'Application info', version='1.0.3')

by_full_path_counter = metrics.counter('full_path_counter', 'counting requests by full path', labels={'full_path': lambda: request.full_path})

by_endpoint_counter = metrics.counter('endpoint_counter', 'counting requestby endpoint', labels={'endpoint': lambda: request.endpoint})

endpoints = ('', 'star', 'api')

JAEGER_AGENT_HOST = os.getenv('JAEGER_AGENT_HOST', 'localhost')

app.config['MONGO_DBNAME'] = 'example-mongodb'
app.config['MONGO_URI'] = 'mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb'

mongo = PyMongo(app)


#Initialize tracing 
def init_tracer(service_name='backend-service'):

    #Logging 
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'logging':True,
        },
        service_name=service_name,
        validate = True,
    )

    return config.initialize_tracer()

tracer = init_tracer('backend-service')

@app.route('/')
@by_full_path_counter
@by_endpoint_counter
def homepage():
    app.logger.info('Hit the homepage')
    with tracer.start_span('homepage-span') as span:
        span.set_tag('homepage-tag', '95')
        return "Hello World"


@app.route('/api')
@by_full_path_counter
@by_endpoint_counter
def my_api():
    app.logger.info('Hit the /api endpoint')
    with tracer.start_span('my_api_span') as span:
        span.set_tag('my_api-tag', '90')
        answer = "something"
        return jsonify(reponse=answer)

@app.route('/star', methods=['POST'])
@by_full_path_counter
@by_endpoint_counter
def add_star():
    app.logger.info('Hit the /star endpoint')

    with tracer.start_span('star_span') as span:
        span.set_tag('star-tag', '80')
        star = mongo.db.stars
        name = request.json['name']
        distance = request.json['distance']
        star_id = star.insert({'name': name, 'distance': distance})
        new_star = star.find_one({'_id': star_id })
        output = {'name' : new_star['name'], 'distance' : new_star['distance']}
        return jsonify({'result' : output})

@app.route('/error')
@by_full_path_counter
@by_endpoint_counter
def oops():
    return ':(', 500

if __name__ == "__main__":
    app.run(threaded=True)
