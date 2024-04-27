import numpy as np
import typing, itertools



import os
import pandas as pd

from typing import Union, List
import boto3
import io
import pickle
from threading import Event, Thread
from flask_executor import Executor
import asyncio
import re
import newrelic.agent


from flask import g
import asyncio




completed_event = Event()





import urllib
from urllib.parse import urlparse
from flask import Flask, render_template_string, request, make_response, render_template, jsonify
from flask_restful import Resource, Api,reqparse, abort
import time
import os
from flask_cors import CORS
from flask_socketio import SocketIO

import pandas as pd
import datetime
import re

from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_transformer

import redis
import pickle
import lightgbm


def initiate_instance():

    return None


app = Flask(
    __name__
)
parser = reqparse.RequestParser()
parser.add_argument('current_time',type=str)


api = Api(app)

executor = Executor(app)
CORS(app)

cors = CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*", "expose_headers": "*"}})


import requests
with app.app_context():
    print('app_context ', app.app_context())
    initiate_instance()
class ds_search_index_init(Resource):
    def get(self):
        # global sch
        # del sch
        try:
            app.config.pop('var_ins')
        except:
            print('var_ins does not exists')

        completed_event.clear()

        # executor.submit(initiate_instance)
        print('##### Data Update is called #####')
        with app.app_context():

            executor.submit(initiate_instance)
        print('##### Data Update is finished #####')

        completed_event.set()
api.add_resource(ds_search_index_init,'/sf_ms/api/cmb/init')


class ds_eta_microservice_container(Resource):
    def get(self):
        # future = executor.submit(initiate_instance)
        # print('completed_event.is_set() : ',completed_event.is_set())
        # print("app.config['sch'] :  ", app.config['sch'])
        # print("app.config : ", app.config )
        # if not (completed_event.is_set() & ('var_ins' in app.config)) :
        #     #completed_event.wait()
        #     #return jsonify({'message':'waiting for the initiation process'}),404
        #     abort(404, message="waiting for the initiation process")
        # else:
        #     st = time.time()
        args = parser.parse_args()
        # print('received search query : ', args['search_keyword'])
        current_time_input_API = args['current_time']

        # data_arg = {'search_keyword': search_query}
        # app.config['var_ins'].current_time = current_time_input_API
        # response = app.config['var_ins'].model_combo()
        response = {}
        response['user input : '] = current_time_input_API

        # response = json.loads(requests.get('http://localhost:5001/search_engine/api/cmb', json=data_arg).text)
        et = time.time()
        time.sleep(5)
        st = time.time()
        time_elapsed = et - st
        response['time elapse'] = str(time_elapsed * 1000) + ' ms'
        return jsonify(response)

api.add_resource(ds_eta_microservice_container,'/sf_ms/api/cmb/timing')




def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# if __name__ == "__main__":
#     #app.run(host='0.0.0.0', port=5001,threaded=True,debug=True)
if __name__ == "__main__":
    # sch = initiate_instance()
    # newrelic.agent.initialize(newrelic_config_file, environment=newrelic_environment,
    #                           distributed_tracing=distributed_tracing_enabled)
    app.run(host='0.0.0.0', port=5001, debug=False,threaded=False)
