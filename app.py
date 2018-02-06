from flask import Flask, jsonify, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('data/graph.json') as f:
    graph = json.load(f)

# For now, only one graph:
@app.route('/')
def draw_graph():
    return jsonify(graph)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
