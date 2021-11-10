from flask import Flask
from flask_cors import CORS, cross_origin
from storage import Storage
import json


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

storage = Storage('172.17.0.2:27017')


@app.route("/lawsuit/<path:endpoint>", methods=["GET"])
@cross_origin()
def query_lawsuit(endpoint):
    return storage.get_lawsuit(endpoint)


if __name__ == '__main__':
    app.run(host="localhost", port=3001)
