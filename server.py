class server:

    def getPersonMessage(self, name, myclient):
        db = myclient["test"]
        cl = db["test"]
        myquery = {"name": name}
        doc = cl.find(myquery)
        for x in doc:
            print(x)

    def add(self, name, message, date, myclient):
        db = myclient["test"]
        cl = db["test"]
        di = {"name": name, "message": message, "date": date}
        cl.insert_one(di)

    def update(self, name, new_message, new_date, myclient):
        db = myclient["test"]
        cl = db["test"]
        query = {"name": name}
        di = {"$set": {"message": new_message, "date": new_date}}
        cl.update_one(query, di, True)

    def delete(self, name, myclient):
        db = myclient["test"]
        cl = db["test"]
        d = {"name": name}
        cl.delete_one(d)