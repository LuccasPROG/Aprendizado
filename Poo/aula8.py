class connection:
    def __init__(self):
        self.host = None
        self.user = None
        self.password = None
    
    
    def set_user(self, user):
        self.user = user


    def set_password(self, password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection



# c1 = connection()
c1 = connection.create_with_auth('lucas', '1234')
# c1.set_user('luiz')
# c1.set_password('123456789')
print(c1.user)
print(c1.password)