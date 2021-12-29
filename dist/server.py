from flask import Flask, jsonify, render_template
from flask_cors import CORS

import argparse

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve():
    return render_template('template.html', dashboard="Test", dashboard_id=app.config['dashboard_id'])


@app.route('/api/name')
def name():
    data = app.config['name']
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


def configure_app(dashboard_id, dashboard_name):
    app.config.update(
        dashboard_id=dashboard_id,
        name=dashboard_name
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Output HTML with name')
    parser.add_argument('dashboard_id', type=str)
    parser.add_argument('name', type=str)   

    args = parser.parse_args()

    configure_app(args.dashboard_id, args.name)

    app.run()