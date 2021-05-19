from flask import Flask, json, request,render_template
from db import *

app = Flask(__name__)


@app.route('/')
def index():
    activity_list = activity.find()
    return render_template('index.html',activity_list=activity_list)


@app.route('/github', methods=['POST'])
def github_api():
    if request.headers['Content-Type'] == 'application/json':
        l = request.json
        print(l)
        if str(l).find('before') != -1 and str(l).find('pull_request') == -1:
            print(l)
            return l
        elif str(l).find('pull_request') != -1 and str(l).find('before') == -1 and l['action']=='opened' :
            pull_req_by = l
            request_id = pull_req_by['pull_request']['id']
            author = pull_req_by['pull_request']['user']['login']
            action = 'PULL_REQUEST'
            from_branch = pull_req_by['pull_request']['head']['label']
            to_branch = pull_req_by['pull_request']['base']['label']
            query = {'request_id': request_id, 'author': author, 'action': action, 'from_branch': from_branch,
                     'to_branch': to_branch}
            print(query)
            pull_ob = Pull(request_id, author, action, from_branch, to_branch)
            pull_ob.commit()

            return l
    return l

if __name__ == '__main__':
    app.run(debug=True)
