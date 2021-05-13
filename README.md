# CNMIMapServer
Small web application to create choropleth maps of the CNMI serverside.

#Installation
1) Git clone to a local directory
2) cd to the directory
3) run: pip install -r requirements.txt in your shell.

#Usage
When the CNMIMapServer.py file is running on the server, http connections will be accepted on port XXXXX, and JSON encoded excel tables can be used to visualize data by submitting a request from your browser using the following URL format:

http://localhost:5000/api/cnmi_map?json=[JSON STRING GOES HERE]
