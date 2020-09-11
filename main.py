from flask import Flask, request, Response
from src.utilities import text_logger, singleton
from src.services import create_summary
import jsonpickle

singleton.Singletons()
logger = text_logger.get_logger("main")

app = Flask(__name__)


@app.route('/get_summary', methods=["POST", "GET"])
def get_summary():
    sentence = request.form.get("text")
    min_len = int(request.args.get("min_len"))
    max_len = int(request.args.get("max_len"))
    result = create_summary.get_summary(sentence, min_len, max_len)
    resp = Response(str(result), status=200,
                    mimetype='application/text')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5010', debug=True)
