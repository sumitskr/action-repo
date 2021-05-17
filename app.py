from flask import Flask , json , request

app = Flask(__name__)

@app.route('/')
def index():
    return "sucess"
@app.route('/github',methods=['POST'])
def github_api():
    if request.headers['Content-Type'] =='application/json':
        return json.dumps(request.json)
    else:
        return "working"
if __name__== '__main__':
    
    app.run(debug=True)
