class Message:
    id = 0
    def __init__(self,clientName , message):
        Message.id += 1
        self.id = Message.id
        self.clientName = clientName 
        self.message = message
    def __str__(self) -> str:
        return "Id : {} Name : {} Message :{} \n".format(self.id , self.clientName ,self.message)