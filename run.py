import logging
import socket
import optparse

from src import start_iperf3_api

log_file = 'iPerf3.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG)
logging.info('Logging into ' + log_file)

default_host = "127.0.0.1"
default_port = 5000

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-H", "--host", help="Hostname/IP for the iPerf3 RestAPI application" + "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port", help="Port for the iPerf3 RestAPI application " + "[default %s]" % default_port,
                      default=default_port)
    options, _ = parser.parse_args()
    try:
        app = start_iperf3_api()
        app.run(debug=True, host=options.host, port=options.port)
        logging.info("iPerf3 Rest API has been started...")
    except socket.error as error:
        logging.warning('iPerf3 Rest API Error: ' + str(error))
    
