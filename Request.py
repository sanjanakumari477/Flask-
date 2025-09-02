from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for GET request

@app.route('/get_example', methods=['GET'])
def get_example():
    name = request.args.get('name', 'Guest')  # Get parameter from URL
    return jsonify({"message": f"Hello, {name}! This is a GET request."})

# Route for POST request

@app.route('/post_example', methods=['POST'])
def post_example():
    data = request.get_json()  # Get JSON data from request body
    name = data.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}! This is a POST request."})

if __name__ == '__main__':
    
    app.run(debug=True)
