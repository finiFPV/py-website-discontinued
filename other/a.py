import pymongo

myclient = pymongo.MongoClient("mongodb://program:q3zXflirw4V%40W9U1AU%23%5ED4%253@192.168.101.100:27017/?authMechanism=DEFAULT")
mydb = myclient["Main"]
mycol = mydb["Users"]
mydict = {"user": "fini", "password": "1234", "email": "markusskalenda@gmail.com", "hardwareid": "03C00218-044D-052E-DD06-9E0700080009", "membership": "none", "admin": True, "owner": False, "time": "28/09/2022 21:34:22", "level": 0, "2fa": False, "remember": False}

x = mycol.insert_one(mydict)