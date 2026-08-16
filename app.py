from flask import Flask

app = Flask(__name__)

fleet = ["Flatiron Crossroads", "Crossroads", "Flatiron Sedan", "Flatiron SUV"]

@app.route('/')
def index():
    return "Welcome to Flatiron Cars"

@app.route('/models/<model_name>')
@app.route('/model/<model_name>')
def show_model(model_name):
    match = next((item for item in fleet if item.lower() == model_name.lower() or model_name.lower() in item.lower()), None)
    if match:
        return f"{model_name} is in our fleet!"
    return f"No models called {model_name} exist in our catalog"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
