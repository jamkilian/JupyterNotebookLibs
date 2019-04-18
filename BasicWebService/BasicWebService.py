from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/addTwoNums", methods=["GET", "POST"])
def addTwoNumbers():
    if request.method == "GET":
        num1 = request.args.get('num1')
        num2 = request.args.get('num2')
        result = float(num1) + float(num2)
    elif request.method == "POST":
        data = json.loads(request.data)
        result = float(data["num1"]) + float(data["num2"])

    return str(result)


if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
