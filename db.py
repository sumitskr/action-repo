# getting mongodb database
import pymongo
import datetime
import pytz
# from wtforms import SubmitField,ValidationError
myclient = pymongo.MongoClient("mongodb+srv://sumit:sumitsarkar@cluster0.c5xwu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

git = myclient.get_database("git")
activity=git.get_collection('req') #getting collection


class Pull:
    def __init__(self, request_id, author, action, from_branch, to_branch):
        self.request_id = request_id
        self.author = author
        self.action = action
        self.from_branch = from_branch
        self.to_branch = to_branch
        self.timestamp = self.timeStamp()

    def timeStamp(self):
        today = datetime.datetime.now(datetime.timezone.utc)

        day = (today.strftime("%d"))
        if 4 <= int(day) <= 20 or 24 <= int(day) <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][int(day) % 10 - 1]
        dayn = day + suffix
        dayn = dayn + today.strftime(" %b %Y - %I:%M %p ") + 'UTC'
        return dayn
    def commit(self,query):
        activity.insert_one(query)
