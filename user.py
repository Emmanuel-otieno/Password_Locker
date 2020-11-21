from credentials import Credentials

class User(Credentials):

    def __init__(self):
        super().__init__()
        self.username =None
        self.password =None
        self.isLoggedIn = False
        if self.isLoggedIn ==False:
            user_input = int(input('Reply with 1 to login or 2 to signup(1/2): '))
            username = input('username:')
            password = input('password:')
            if user_input == 1:
                self.sign_in(username,password)
            self.create_new_user(username,password)  


    def create_new_user(self,username,password):
        self.username = username
        self.password = password
        print("Account created successfully")
        self.isLoggedIn = True


    def view_accounts(self):
        for ac in self.accounts:
            print(ac)
        return self.accounts  


    def sign_in(self,username,password):
        if username == self.username and password == self.password:
            self.isLoggedIn = True
            print('success')
            return "Login successfully"
        else:
            print('Login failed')  
            return "incorrect username"

            
              



