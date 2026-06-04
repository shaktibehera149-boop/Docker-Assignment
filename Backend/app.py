from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():

    data = request.json

    return jsonify({
        "name": data["name"],
        "email": data["email"],
        "message": "Data Received"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)