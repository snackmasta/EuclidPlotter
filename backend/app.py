from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

# Example in-memory storage (could be a database)
stars = []

# Route to handle adding a star
@app.route('/add_star', methods=['POST'])
def add_star():
    data = request.json
    stars.append(data)
    return jsonify({'message': 'Star added!', 'data': data})

# Route to handle fetching all stars
@app.route('/get_stars', methods=['GET'])
def get_stars():
    return jsonify(stars)

# Route to serve the frontend HTML file
@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

# Route to serve the favicon (optional)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

# Ensure that static files like JS and CSS are served
@app.route('/<path:path>')
def serve_static_file(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Create a static directory if it doesn't exist
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
