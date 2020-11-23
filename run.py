#!/usr/bin/env python3.8

from user import User
from credentials import Credentials 

def create_account(account_name,user_name,password,email):
    '''
    Function to create a new account
    '''
    new_account = User(account_name,user_name,password,email)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()    

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()  

def find_account(name):
    '''
    Function that finds a account
    '''
    return User.find_by_name(name) 

def check_existing_accounts(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return User.account_exist(name) 


def create_credentials(credentials_name,name,password,email):
    '''
    Function to create a new account
    '''
    new_credentials = Credentials(credentials_name,name,password,email)
    return new_credentials 

def save_credentials(credentials):
    '''
    Function to save account
    '''
    credentials.save_credentials()  

def del_credentials(credentials):
    '''
    Function to delete a account
    '''
    credentials.delete_credentials()    

def find_credentials(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Credentials.find_by_name(name)  

def check_existing_credentials(name):
    
    return Credentials.credentials_exist(name) 

def display_credentials():  
    '''
    Function that help in view all the saved accounts
    '''
    return Credentials.display_credentials() 



def main():
    print("WELCOME TO PASSWORD LOCKER ENTER YOUR NAME")
    user_name = input()
    print(f"Hello {user_name}, sign up to password locker to create an account")
    print('\n')

    while True:
     print("Use these known short codes : up -> SIGN UP new account, in ->LOGIN to your account, ex ->exit PassWord Locker.")   
     short_code = input().lower()

     if short_code == 'up':
            print("Create your account")
            print("_"*100)
            account_name = input('Account name:')
            print ('\n')
            u_name = input('User name:')
            print ('\n')
            pwd = input('Password : ')
            print ('\n')
            e_address = input('Email address:')
            save_accounts(create_account(account_name,u_name,pwd,e_address)) 
            print ('\n')
            print(f"A New {account_name} Account with the user name  {u_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')
     elif short_code == "ex":
            print(f"Thanks {user_name} for trying our password locker")
            break
            

     elif short_code == 'in':
            print("Enter your password to login.")
            search_account = input()
            if check_existing_accounts(search_account):
                print("\033[1;32;1m   \n")
                print(f"Your account {account_name} has been logged out succesfully")
                print("\033[1;37;1m   \n")  

                while True:
                    print('''Use these short codes:
                    ca -> Create new credential.
                    ex ->Log out your credentials account. ''')
                    short_code = input().lower()
                    if short_code == "ca":
                        print("Create new credential")
                        print('_' * 20)
                        credentials_name = input('Credential name:')
                        print('\n')
                        usr_name = input(f"{credentials_name} user name:")
                        print('\n')
                        print('*' * 20)
                        pwd = input(f"{credentials_name} password:")
                        save_credentials(create_credentials(credentials_name,u_name,pwd,e_address))
                        print('\n')
                        print(f"A New {credentials_name} Account with the user name  {usr_name} has been created.")
                        print ('\n')  

                    elif short_code == 'ds':
                         if display_credentials():
                             print("Here is your credentials")
                             print('\n')
                             for credentials in display_credentials():
                                 print(f"Credential name:{credentials.credentials_name}  User name: {credentials.name} Password:{credentials.password}")
                                 print('\n')
                         else:
                              print('\n')
                              print("create an account first")
                              print('\n')  

                    elif short_code == "ex":
                        print('\n')
                        print(f"Your account {account_name} has been logged out successfully")
                        print('\n')
                        break
         
     else:
        print("confirm your selection and try again") 
        print('\n')    


if __name__ == "__main__":
    main()             