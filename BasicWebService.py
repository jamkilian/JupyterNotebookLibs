from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/addTwoNums", methods=['POST'])
def addTwoNumbers():
    data = json.loads(request.data)
    # num1 = request.args.get('num1')
    # num2 = request.args.get('num2')
    result = float(data["num1"]) + float(data["num2"])
    return str(result)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
