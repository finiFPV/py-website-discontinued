class DB:
    def __init__(self, collection="Users"):
        from pymongo import MongoClient
        self.client = MongoClient("mongodb://program:q3zXflirw4V%40W9U1AU%23%5ED4%253@192.168.101.100:27017/?authMechanism=DEFAULT")["Main"][collection]
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