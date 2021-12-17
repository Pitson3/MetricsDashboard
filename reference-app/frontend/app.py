from flask import Flask, render_template, request

import logging
from jaeger_client import Config
import time
import random
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)


#static information as metric. Adapted from https://github.com/rycus86/prometheus_flask_exporter/blob/master/examples/sample-signals/app/app.py
metrics.info('app_info', 'Application info', version='1.0.3')

by_full_path_counter = metrics.counter('full_path_counter', 'counting requests by full path', labels={'full_path': lambda: request.full_path})

by_endpoint_counter = metrics.counter('endpoint_counter', 'counting requestby endpoint', labels={'endpoint': lambda: request.endpoint})

#Initilaize tracing 
def init_tracer(service_name='frontend-service'):

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


tracer = init_tracer('frontend-service')

@app.route('/')
@by_full_path_counter
@by_endpoint_counter
def homepage():
    with tracer.start_span('homepage-span') as span:
        span.set_tag('homepage-tag', '90')
        return render_template("main.html")
    



if __name__ == "__main__":
    app.run(threaded=True)