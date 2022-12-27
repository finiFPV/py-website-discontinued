from pymongo import MongoClient
from datetime import datetime

class DB:
    def __init__(self, collection="Users"):
        self.client = MongoClient("***REMOVED***")["Website"][collection]
    def search_user(self, username):
        results = self.client.find({"user": username})
        results = [credentials for credentials in results]
        if len(results) > 0:
            user_found = True
            credentials = results[0]
        else:
            user_found = False
            credentials = {}
        return user_found, credentials
    def update_user(self, username, field, data):
        self.client.update_one({'user': username}, {'$set': {field: data}})
    def insert_data(self, username, password):
        self.client.insert_one({
            "user": username,
            "pswd": password,
            "membership": None,
            "admin": False,
            "owner": False,
            "last_login": None,
            "reg_time": datetime.now().strftime("%Y.%m.%d %H:%M:%S")
            })


class Account:
    class Main:
        @staticmethod
        def login(username, password):
            results = DB().search_user(username)
            if results[0] == False:
                return 404
            elif results[1]["pswd"] == password:
                DB().update_user(username, "last_login", datetime.now().strftime("%Y.%m.%d %H:%M:%S"))
                return results
            else:
                return 401

        @staticmethod
        def register(username, password):
            results = DB().search_user(username)
            if results[0] == False:
                DB().insert_data(username, password)
                if DB().search_user(username)[1]["user"] == username:
                    return 201
                else:
                    return 404
            else:
                return 302