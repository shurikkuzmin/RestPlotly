from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

#@app.route("/")
api.add_resource(HelloWorld,'/')

if __name__=="__main__":
    app.run(debug=True)
#def hello_world():
#    return "<p>Hello, World!</p>"

