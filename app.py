from flask import Flask , json , request

app = Flask(__name__)

@app.route('/')
def index():
    return "sucess"
@app.route('/github',methods=['POST'])
def github_api():
    if request.headers['Content-Type'] =='application/json':
        l=json.dumps(request.json)
        replaced_data=l.replace('true','True')
        replaced_data=replaced_data.replace('false','False')
        replaced_data=replaced_data.replace('null','None')
        print("working")
        print(type(replaced_data))
        print(replaced_data)
        return replaced_data
    else:
        return "working"
if __name__== '__main__':
    
    app.run(debug=True)
