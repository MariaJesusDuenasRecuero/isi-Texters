import json
from os import path

USERS_PATH = path.join(path.dirname(__file__), "users.json")

class BrokerSingleton(object):
    
    __instance = None

    def __new__(cls):
        if BrokerSingleton.__instance is None:
            BrokerSingleton.__instance = object.__new__(cls)
            
        return BrokerSingleton.__instance
    
    def __init__(self):
        with open(USERS_PATH, 'r') as f:
            self.users = json.load(f)
            
    def readUser(self, user):
        for u in self.users["users"]:
            if user.email == u["email"] and user.password == u["password"]:
                print(user.email)
                print(user.password)
                return u
            
        raise Exception("Este usuario no existe") 
                
    def get_instance(self):
        return self.__instance
    
    