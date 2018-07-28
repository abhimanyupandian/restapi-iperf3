import iperf3
import threading

from src.utils.data import status
from flask import make_response, jsonify

def get_status(_o):
    for each in threading.enumerate():
        _t = getattr(each, '_args') if hasattr(each, '_args') else getattr(each, '_Thread__args')
        for _x in _t:
            if ((type(_x) is iperf3.iperf3.Server) or (type(_x) is iperf3.iperf3.Client)):
                if (_o._test == _x._test):
                    return status(_o, _x)
    return status(_o, None)
    
def response(_message, _code):
    return make_response(jsonify(_message), _code) 
    