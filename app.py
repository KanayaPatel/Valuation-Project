import flask
from flask import request
import ProjectFunc as pf

app = flask.Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    print(" -- [DEBUG] Entering Index Page -- ")
    return flask.render_template('valuation.html')

@app.route('/valuation')
def valuation(): 
    return flask.render_template('valuation.html')

@app.route("/process", methods=["POST"])
def process(): 
    data = request.json

    ticker = data.get("ticker_sym")
    time_period = data.get("period")
    amount = data.get("time_amount")
    data_type = data.get("d_type")
    steps = data.get("step")

    total_time = amount + time_period
    val_data = pf.get_data(ticker, total_time, data_type)
    
    conf_int = pf.confidence_intervals(data=val_data, n_iter=50, step=steps)
    low_int = conf_int[0][0]
    high_int = conf_int[0][1]

    result = {"min": low_int, "max": high_int}
    return flask.jsonify(result=result)

def main(): 
    app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == '__main__':
    main()