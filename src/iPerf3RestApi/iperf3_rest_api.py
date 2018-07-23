import json
import iperf3
import socket
import logging
import optparse
import threading

from flask import Flask, request, make_response, jsonify
from ConnectionCache import ConnectionCache

app = Flask(__name__)
log_file = 'iPerf3.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG)
logging.info('Logging into ' + log_file)


_servers = ConnectionCache()
_clients = ConnectionCache()


def _success(data):
    return {
        "data": data
    }


def _error(message):
    return {
        "error": {
            "message": message
            }
        }


default_host = "127.0.0.1"
default_port = 5000


@app.route("/server/create", methods=['POST'])
def create_server():
    if request.headers['Content-Type'] == 'application/json':
        name = str(request.json['name'])
    else:
        return make_response(jsonify(_error("Server creation Failed : Please provide Server 'name'!"))), 500
    server = iperf3.Server()
    server.json_output = False
    _servers.register(server, name)
    return make_response(jsonify(_success(request.data)), 201)


@app.route("/server/<name>/run", methods=['POST', 'PATCH'])
def run_server(name):
    try:
        server = _servers.get_connection(str(name))
        _thread = threading.Thread(target=server.run)
        _thread.daemon = True
        _thread.start()
        return make_response(jsonify(_success(name + " was started")), 200)
    except Exception as e:
        return make_response(jsonify(_error("Server to start Client '" + name + "' : " + str(e))), 500)


@app.route("/server/<name>", methods=['PATCH'])
def set_server(name):
    try:
        server = _servers.get_connection(str(name))
        if request.headers['Content-Type'] == 'application/json':
            for _param, _value in request.json.iteritems():
                if hasattr(server, _param):
                    setattr(server, str(_param), _value)
    except Exception as e:
        return make_response(jsonify(_error("Unable to PATCH to Server - " + name + "! Error:" + str(e))), 500)
    return make_response(jsonify(_success(request.json)), 200)


@app.route("/client/create", methods=['POST'])
def create_client():
    if request.headers['Content-Type'] == 'application/json':
        name = str(request.json['name'])
    else:
        return make_response(jsonify(_error("Client creation Failed : Please provide Client name!"))), 500
    client = iperf3.Client()
    _clients.register(client, name)
    return make_response(jsonify(_success(request.data)), 201)


@app.route("/client/<name>/run", methods=['POST', 'PATCH'])
def run_client(name):
    try:
        client = _clients.get_connection(str(name))
        results = client.run()
    except Exception as e:
        return make_response(jsonify(_error("Unable to start Client '" + name + "' : " + str(e))), 500)
    return make_response(jsonify(_success(results.json), 200))


@app.route("/client/<name>", methods=['PATCH'])
def set_client(name):
    try:
        client = _clients.get_connection(str(name))
        if request.headers['Content-Type'] == 'application/json':
            for _param, _value in request.json.iteritems():
                if hasattr(client, _param):
                    setattr(client, str(_param), _value)
    except Exception as e:
        return make_response(jsonify(_error("Unable to PATCH to Client - " + name + "! Error:" + str(e))), 500)
    return make_response(jsonify(_success(request.json)), 200)


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host", help="Hostname of iPerf3 RestAPI app " + "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port", help="Port for the iPerf3 RestAPI app " + "[default %s]" % default_port,
                      default=default_port)
    options, _ = parser.parse_args()
    try:
        app.run(debug=True, host=options.host, port=options.port)
    except socket.error as error:
        logging.warning('iPerf3Api Error: ' + str(error))
