class database:
    def insert(self,a,b):
        file=open("testing","w")
        file.write(a)
        file.close()
        import pymongo
        from pymongo import MongoClient
        client = pymongo.MongoClient("mongodb+srv://ShivamSrivastava:8960278492@cluster0.e7t1u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client["Educate"]
        collection = db["yourself"]
        collection.insert_one({a:b})