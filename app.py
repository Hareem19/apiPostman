from flask import Flask, jsonify, request

app = Flask(__name__)
nums=[1,2,3,4,5]
@app.route('/')
def hello():
    return "<h1>Hello, World!<h1>"

@app.route("/evenOdd<int:num>")
def evenOdd(num):
    status = None
    if num % 2 == 0:
        status = "Even"
    else:
        status = "Odd"
    
    return jsonify({'status': status})
@app.route("/addnum",methods=["POST"]) 
def addnum():
    request_data=request.get_json()
    print(request_data["num"])
    nums.append(request_data["num"])
@app.route("/showList")
def show():
    return jsonify({"list":nums})















9
if __name__ == '__main__':
    app.run(debug=True)
