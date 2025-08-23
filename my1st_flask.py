from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def home():
    return "Hello, World! Welcome to Flask."

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
