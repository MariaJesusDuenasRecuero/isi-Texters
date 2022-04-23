import os, sys

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)

from model.userDAO import UserDAO

class User:
    
    def __init__(self, email, password, name=None, subscribed=False):
        self.email = email
        self.password = password
        self.name = name
        self.subscribed = subscribed
        self.userDao = UserDAO()
        
    def read_user(self):
        try:
            user_json = self.userDao.read_user(self)
        except Exception as e:
            raise e
        else:
            self.name = user_json["name"]
            self.password = user_json["password"]
            self.email = user_json["email"]
            self.subscribed = user_json["subscribed"]
    
    def create_user(self):
        if self.userDao.read_user == None: #si no lo puede leer, es que no existe, se crea
            self.userDao.create_user(self.name, self.password, self.email, self.subscribed)
    
    def update_user(self):
        self.userDao.update_user()
        
    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "subscribed": self.subscribed,
            "password": self.password
        }
    
    