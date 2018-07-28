import threading

from iperf3.iperf3 import Server
from iperf3.iperf3 import Client
from src.utils.Cache import Cache
from src.utils.data import success, failure
from src.utils.functions import get_status, response

from flask import request
from flask import Blueprint
bp = Blueprint('iPerf3RestApi', __name__, url_prefix='/')

_servers = Cache()
_clients = Cache()

@bp.route("/server/create", methods=['POST'])
def create_server():
    if request.headers['Content-Type'] == 'application/json':
        name = str(request.json['name'])
    else:
        return response(failure("Server creation Failed : Please provide Server 'name'!"), 500)
    server = None
    try:
        server = Server()
        _servers.register(server, name)
        if server:
            return response(success(request.data), 201) 
        else:
            raise Exception("(" + str(server._errno) + ") " + str(server._error_to_string(server._errno)))
    except Exception as error:
        return response(failure("Server '" + name + "' creation failed : " + str(error)), 500)

@bp.route("/server/<name>/run", methods=['POST'])
def run_server(name):
    try:
        server = _servers.get_connection(str(name))
        _thread = threading.Thread(target=server.run)
        _thread.daemon = True
        _thread.start()
        if server._errno == 0:
            return response(success(name + " was started!"), 200)
        else:
            raise Exception("(" + str(server._errno) + ") " + str(server._error_to_string(server._errno)))
    except Exception as e:
        return response(failure("Unable to start Server '" + str(name) + "' : " + str(e)), 500)

@bp.route("/server/<name>/status", methods=['GET'])
def server_status(name):
    try:
        server = _servers.get_connection(str(name))
        status = get_status(server)
        return response(success(status), 200)
    except Exception as e: 
        return response(failure("Unable to get status of Server '" + str(name) + "' : " + str(e)), 500)

@bp.route("/server/<name>", methods=['PATCH'])
def set_server(name):
    try:
        server = _servers.get_connection(str(name))
        if request.headers['Content-Type'] == 'application/json':
            for _param, _value in request.json.iteritems():
                if hasattr(server, _param):
                    setattr(server, str(_param), _value)
    except Exception as error:
        return response(failure("Unable to PATCH Server - " + name + "! Error:" + str(error)), 500)
    return response(success(request.json), 200)

@bp.route("/client/create", methods=['POST'])
def create_client():
    if request.headers['Content-Type'] == 'application/json':
        name = str(request.json['name'])
    else:
        return response(failure("Client creation Failed : Please provide Client name!"), 500)
    client = None
    try:
        client = Client()
        _clients.register(client, name)
        if client:
            return response(success(request.data), 201)
        else:
            raise Exception("(" + str(client._errno) + ") " + str(client._error_to_string(client._errno)))
    except Exception as error:
        return response(failure("Client '" + name + "' creation failed : " + str(error)), 500)

@bp.route("/client/<name>/run", methods=['POST'])
def run_client(name):
    try:
        client = _clients.get_connection(str(name))
        try:
            results = client.run()
        except IndexError:
            raise Exception(str("Please check if the Server ("+client.server_hostname+":"+str(client.port)+") is up!"))
        except Exception as e:
            raise Exception(e)
        if client._errno == 0:
            return response(success(results.json), 200)
        else:
            raise Exception("(" + str(client._errno) + ") " + str(client._error_to_string(client._errno)))
    except Exception as error:
        return response(failure("Unable to start Client '" + name + "' : " + str(error)), 500)
 
@bp.route("/client/<name>", methods=['PATCH'])
def set_client(name):
    try:
        client = _clients.get_connection(str(name))
        if request.headers['Content-Type'] == 'application/json':
            for _param, _value in request.json.iteritems():
                if hasattr(client, _param):
                    setattr(client, str(_param), _value)
    except Exception as error:
        return response(failure("Unable to PATCH to Client - " + name + "! Error:" + str(error)), 500)
    return response(success(request.json), 200)

@bp.route("/client/<name>/status", methods=['GET'])
def client_status(name):
    try:
        client = _clients.get_connection(str(name))
        status = get_status(client)
        return response(success(status), 200)
    except Exception as error:
        return response(failure("Unable to get status of Client '" + name + "' : " + str(error)), 500)

