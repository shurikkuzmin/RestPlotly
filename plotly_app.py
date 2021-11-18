import flask
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

#api.add_resource(TodoSimple, '/<string:graph_id>')
@app.route("/", methods=["GET"])
def get_data():
    print("graphs from get", graphs)
    return flask.render_template("graph.html", graphs = graphs)

@app.route("/", methods=["PUT","POST"])
def put_data():
    #print(request)
    graph = request.form['data']
    print(graph)
    #graphs.append(graph.data)    
    return jsonify(graph)
 
if __name__=="__main__":
    app.run(debug=True)