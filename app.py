from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)



# For now, only one graph:
@app.route('/')
def draw_graph():
    return 'Hello'

@app.route('/graph1')
def draw_graph1():
    with open('data/graph1.json') as f:
        graph = json.load(f)
    return jsonify(graph)

@app.route('/graph2')
def draw_graph2():
    with open('data/graph2.json') as f:
        graph = json.load(f)
    return jsonify(graph)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
