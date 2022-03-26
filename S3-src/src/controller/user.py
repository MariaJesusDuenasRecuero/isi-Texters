from model.userDAO import UserDAO


class User:
    
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
        self.subscribed = False
        self.userDao= UserDAO
        
    def read_user(self):
        self.userDao.read_user()
    
    def create_user(self):
        if self.userDao.read_user == None: #si no lo puede leer, es que no existe, se crea
            self.userDao.create_user(self.name, self.password, self.email, self.subscribed)
    
    def update_user(self):
        self.userDao.update_user()
    
    