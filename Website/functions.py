class DB:
    def __init__(self, collection="Users"):
        from pymongo import MongoClient
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

    def insert_data(self, username, password):
        self.client.insert_one({"user": username, "pswd": password})


class Account:
    class Main:
        @staticmethod
        def login(username, password):
            results = DB().search_user(username)
            if results[0] == False:
                return 404
            elif results[1]["pswd"] == password:
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