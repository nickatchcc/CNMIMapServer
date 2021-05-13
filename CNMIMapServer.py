# Source code credit Yash Sanghvi (https://medium.com/tech-carnot/interactive-map-based-visualization-using-plotly-44e8ad419b97)

from os import environ
import os
import sys

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
import json

import pandas as pd
import plotly
import plotly.express as px
import plotly.io as pio
plotly.io.orca.config.executable = r"C:\Users\username\AppData\Local\Programs\orca\orca.exe" # application server specific
import datetime as d

# Initialize Flask
app = Flask('__main__', static_folder=os.path.abspath(r'C:\source\repos\CNMIMapServer')) # application server specific
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('json')

class cnmi_map(Resource):

    def map(self,values):
        content = request.json
        df = pd.read_json(values)
        with open('rota_saipan_tinian.json') as f: cnmi = json.load(f)
        #with open('cnmi.json') as f: cnmi = json.load(f) #northern islands unpopulated based on best information available to me at time of publication

        cnmi["features"][0]['properties']
        #max_value = 1.0 # Default setting is 1.0 as max value
        max_value = df["Value"].max()
        fig = px.choropleth(df, geojson=cnmi, locations='NAMELSAD', color='Value', #change 'Value' to the name of the column describing color temperature
                    color_continuous_scale="Viridis",range_color=(0, max_value),
                    featureidkey="properties.NAMELSAD", projection="mercator")
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        fig.update_layout(autosize=True, width=1900, height=750,)
        for i in range(0, len(cnmi["features"])): 
            print(cnmi["features"][i]["properties"]["NAMELSAD"])
        fig.write_html(r'.\choropleth.html')
        self.injectJS()

    def get(self):
        data = parser.parse_args()
        self.map(data['json'])
        return app.send_static_file('choropleth.html')
      
    def injectJS(self):
        a = """<script type="module">
        </script>"""
        
        with open(r'.\choropleth.html', 'r+') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith('<body>'):
                    lines[i] = lines[i]+a
            f.truncate()
            f.seek(0)
            for line in lines:
                f.write(line)

api.add_resource(cnmi_map, '/api/cnmi_map')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=14515)
