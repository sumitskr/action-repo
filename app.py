from flask import Flask , json , request
import datetime


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
app = Flask(__name__)

@app.route('/')
def index():
    return "sucess"
@app.route('/github',methods=['POST'])
def github_api():
    if request.headers['Content-Type'] =='application/json':
        l=request.json
        print(l)
        print(type(l))

        x = datetime.datetime.now()
        print('logger',x)

        return l
if __name__== '__main__':
    
    app.run(debug=True)
