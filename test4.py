from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/test', methods=['POST'])
def test():
    print("test pass")
    return jsonify({'test': 'pass'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
