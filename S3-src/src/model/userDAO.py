import os, sys

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)

from model.broker import BrokerSingleton

class UserDAO:
    
    def __init__(self) -> None:
        self.broker = BrokerSingleton().get_instance()
    
    def read_user(self, user):
        try:
            return self.broker.readUser(user)
        except Exception as e:
            raise e 
    
    def create_user(self):
        pass
    
    def update_user(self):
        pass  