import logging

from flask import Flask
from src.iPerf3RestApi import bp

def start_iperf3_api():
    try:
        app = Flask("iPerf3 Rest API")
        app.register_blueprint(bp)
        return app
    except Exception as error:
        logging.warning('iPerf3 Rest API Error: ' + str(error))

