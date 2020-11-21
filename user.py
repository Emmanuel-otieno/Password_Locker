
class Credetials:
    def __init__(self):
        self.account =[]

    def new_account(self, accont_name,username,password=None):
        if password is None:
            user_input = int(input('specify the length of password needed: ')) 
            password = self.create_password(user_input) 
            account = ('account_naame':account_name,'username':username,'password':password)
            self.account.append(account)
            print("your account is created sucessfully")
            return account


    def  create_password(self,length=6):
        alphabet = ascli_letters + digits + punctuation
        return "".join( choice(alphabet) for i in range(length))
        