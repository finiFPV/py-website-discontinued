class DB:
    def __init__(self, collection="Users"):
        from pymongo import MongoClient
        self.client = MongoClient("***REMOVED***")["Main"][collection]
    def search_user(self, username):
        results = self.client.find({'user': username})
        results = [credentials for credentials in results]
        if len(results) > 0:
            user_found = True
            credentials = results[0]
        else: 
            user_found = False
            credentials = {}
        return user_found, credentials
def login(username, password):
    #results = DB().search_user(username)
    results = [True]
    if results[0] == False: return 404
    else: return results