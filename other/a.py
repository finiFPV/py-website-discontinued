import pymongo

myclient = pymongo.MongoClient("***REMOVED***")
mydb = myclient["Main"]
mycol = mydb["Users"]
mydict = {"user": "fini", "password": "1234", "email": "***REMOVED***", "hardwareid": "***REMOVED***", "membership": "none", "admin": True, "owner": False, "time": "28/09/2022 21:34:22", "level": 0, "2fa": False, "remember": False}

x = mycol.insert_one(mydict)