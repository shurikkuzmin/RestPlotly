import flask
import json
from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

graphs = []

#class Graph(Resource):
#    def get(self, label):
#        return {label: graphs[label]}

#    def put(self, label):
#        graphs[label] = request.form['data']
#        return {label: graphs[label]}


graphs = {}
@app.route("/", methods=["GET"])
def get_data():
    #graphs=[{"x":[1,2,3],"y":[10,9,8],"mode": "Scatter", "name":"test"},{"x":[10,12,13],"y":[1,2,3],"name":"test2","mode":"Scatter"}]    
    for name in graphs:
        print(graphs[name])
    html_graphs = [{"x": graphs[name]["x"],"y": graphs[name]["y"], "name": name } for name in graphs]
    print("html_graphs=", html_graphs)

    return flask.render_template("graph.html", graphs=html_graphs)

@app.route("/", methods=["POST"])
def put_data():
    # Use the line below if request comes through usual POST
    #graph = request.form['data']
    #graph = json.loads(graph)
    graph = request.get_json()
    print(graph)
    for name in graph:
        if name not in graphs:
            graphs[name]={"x":[], "y":[]}    
        graphs[name]["x"].extend(graph[name]["x"])
        graphs[name]["y"].extend(graph[name]["y"])

    html_graphs = [{"x": graphs[name]["x"],"y": graphs[name]["y"], "name": name } for name in graphs]
    print("html_graphs=", html_graphs)
    return flask.render_template("graph.html", graphs=html_graphs)
 
if __name__=="__main__":
    app.run(debug=True)