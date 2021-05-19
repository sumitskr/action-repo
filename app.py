from flask import Flask, json, request
from db import *
app = Flask(__name__)


@app.route('/')
def index():
    return "sucess"


@app.route('/github', methods=['POST'])
def github_api():
    if request.headers['Content-Type'] == 'application/json':
        l = request.json
        print(l)
        if str(l).find('pull_request')==True and str(l).find('before')==True:
            print("its merge")
            return l
        elif str(l).find('before')==True and str(l).find('pull_request')==False:
            print("push")
            return l
        elif str(l).find('pull_request')==True and str(l).find('before')==False:
            pull_req_by=l
            request_id = pull_req_by['pull_request']['id']
            author = pull_req_by['pull_request']['user']['login']
            action = 'PULL_REQUEST'
            from_branch = pull_req_by['pull_request']['head']['label']
            to_branch = pull_req_by['pull_request']['base']['label']
            query = {'request_id': request_id, 'author': author, 'action': action, 'from_branch': from_branch,
                     'to_branch': to_branch}
            print(query)
            pull_ob=Pull(request_id,author,action,from_branch,to_branch)
            pull_ob.commit()

            return l


if __name__ == '__main__':
    app.run(debug=True)
