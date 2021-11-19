from flask import Flask
from flask_cors import CORS, cross_origin
from storage import Storage


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

storage = Storage('172.17.0.2:9200')


@app.route("/lawsuit/<path:endpoint>", methods=["GET"])
@cross_origin()
def query_lawsuit(endpoint):
    return storage.search_lawsuits(endpoint)


if __name__ == '__main__':
    app.run(host="localhost", port=3001)
