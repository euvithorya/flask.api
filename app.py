from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_message():

    return jsonify({"message": "Hello, this is your first Flask API!"})

if __name__ == '__main__':
    app.run(debug=True)

#:V