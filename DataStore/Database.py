from DataStore.Message import Message
class Database:
    def __init__(self):
        self.store = []
    def insert(self,messObj : Message):
        self.store.append(messObj)
    def remove(self,id):
        del self.store[id]
    def getAll(self):
        return self.store