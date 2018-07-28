# restapi-iperf3 - UNDER DEVELOPMENT
0. To install : python setup.py install

1. Run the API Server APP and run in background: 
  python run.py &

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

8. Get the status of the Server using /server/<server_name>/status:
  curl -H "Content-type: application/json" -X GET http://127.0.0.1:5000/server/server1/status

9. Get the status of the Client using /client/<client_name>/status:
  curl -H "Content-type: application/json" -X GET http://127.0.0.1:5000/client/client1/status

