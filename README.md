# restapi-iperf3 - UNDER DEVELOPMENT

1. Run the API Server APP and run in background: 
  python iperf3_api.py &

2. Create a Server using POST /server/create:
  curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/server/create -d '{"name":"server1"}'
  
3. Modify Server parameters using PATCH /server/<server_name>:
  curl -H "Content-type: application/json" -X PATCH http://127.0.0.1:5000/server/server1 -d '{"bind_address":"127.0.0.1", "port":"5201"}'
  
4. Start the Server using POST /server/<server_name>/run:
  curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/server/server1/run -d '{}'

5. Create a Client using /client/create:
  curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/client/create -d '{"name":"client1"}'

6. Modify Client parameters using PATCH /client/<client_name>:
  curl -H "Content-type: application/json" -X PATCH http://127.0.0.1:5000/client/client1 -d '{"duration":2, "port":5201, "server_hostname":"127.0.0.1"}'
  
7. Start the Client Traffic using /client/<client_name>/run:
  curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/client/client1/run -d '{}'
  
The following are the methods available in the original iperf.py file which will require API methods to be developed.

Client:

1. role - GET - 'c'
2. bind_address - GET and PATCH - IP
3. port - GET and PATCH - int
4. json_output - GET and PATCH - bool
5. verbose - GET and PATCH - bool
6. _errno - GET - Error ID
7. iperf_version - GET - Iperf version
8. _error_to_string - GET - str
9. server_hostname - GET and PATCH - IP address
10. protocol - GET and PATCH - 'tcp' or 'udp'
11. duration - GET and PATCH - int 
12. bandwidth - GET and PATCH - int
13. blksize - GET and PATCH - int
14. num_streams - GET and PATCH - int
15. zerocopy - GET and PATCH - bool
16. reverse - GET and PATCH - bool
17. run - PATCH 

Server:

1. role - GET - 's'
2. bind_address - GET and PATCH - IP
3. port - GET and PATCH - int
4. json_output - GET and PATCH - bool
5. verbose - GET and PATCH - bool
6. _errno - GET - Error ID
7. iperf_version - GET - Iperf version
8. _error_to_string - GET - str
9. run - PATCH
		
