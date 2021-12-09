from flask import Flask, request
from flask_cors import CORS, cross_origin
from searchengine import SearchEngine


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

se = SearchEngine('juslite_elastic:9200')


@app.route("/lawsuit/<path:endpoint>", methods=["GET"])
@cross_origin()
def query_lawsuit(endpoint):
    return se.get_results(endpoint, request.args['sort'])


if __name__ == '__main__':
    app.run(host="localhost", port=3001)
