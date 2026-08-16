existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

# Default route introducing the company
@app.route('/')
def home():
    return "Welcome to the Car Company Database!"

# Route for requesting a specific car model
@app.route('/cars/<model>')
def get_car_model(model):
    return f"Here is the information for the requested model: {model}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)