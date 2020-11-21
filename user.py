
class Credetials:
    def __init__(self):
        self.account =[]

    def new_account(self, accont_name,username,password=None):
        if password is None:
            user_input = int(input('specify the length of password needed: ')) 
            password = self.generate_password(user_input) 
            account = ('account_naame':account_name,'username':username,'password':password)
            self.account.append(account)
            print("your account is created sucessfully")
            return account