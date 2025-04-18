
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/mojastrona')
def moja_strona():
    return "To jest moja strona!"

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

@app.route('/api/v1.0/predict')
def predict():
    try:
        x1 = float(request.args.get('num1'))
        x2 = float(request.args.get('num2'))
    except (TypeError, ValueError):
        return jsonify({"error": "Błędne dane wejściowe. Podaj liczby num1 i num2"}), 400

    wynik = 1 if (x1 + x2) > 5.8 else 0

    return jsonify({
        "prediction": wynik,
        "features": {
            "num1": x1,
            "num2": x2
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
