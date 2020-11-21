
from user import User

def main():
    while True:
        print ("Welcom to password locker")
        print("\n")
        print("select a short code to navigate through:to login'in',to exit'ex': to creat a new user 'nw'")
        short_code = input().lower()
        print("\n")

        if short_code == 'nw':
            print("create username")
            create_user_name = input(any)

            print("create password")
            create_user_name = input(any)

            print("confirm password")
            confirm_password = input()


        if  confirm_password != created_user_password:
            print("Invalid password")
            print("Input password")
            created_user_password = input()
            print ("confirm your password")
            confirm_password = input()


        