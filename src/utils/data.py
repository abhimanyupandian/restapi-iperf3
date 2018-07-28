import iperf3

def success(data):
    return {
        "data": data
        }

def failure(message):
    return {
        "error": {
            "message": message
            }
        }

def status(_o, _s):
    return {
        "error_code" : _o._errno,
        "id": _o._test,
        "error_message" : str(_o._error_to_string(_o._errno)),
        "running": True if _s else False,
        "type": 'server' if (type(_o) is iperf3.iperf3.Server) else 'client'
    }
