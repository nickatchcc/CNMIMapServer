# CNMIMapServer
Small web application to create choropleth maps of the CNMI serverside.

# Installation
1) Git clone to a local directory from cmd.exe (e.g. 'C:\Users\username> git clone https://github.com/nickatchcc/CNMIMapServer.git')
2) cd to the directory (e.g. 'C:\Users\username> cd CNMIMapServer')
3) Install dependencies with pip (e.g. 'C:\Users\username> pip install -r requirements.txt')

# Usage
When the CNMIMapServer.py file is running on the server, http connections will be accepted on port XXXXX, and JSON encoded excel tables can be used to visualize data by submitting a request from your browser using the following URL format:

http://localhost:5000/api/cnmi_map?json=JSON_STRING_GOES_HERE
