#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(login_username,password):
    '''
    Function to create a new user
    '''
    new_user = User(login_username,password)
    return new_user


def create_credentials(username_name,account_name,account_password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(username_name,account_name,account_password)
    return new_credentials  

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()    

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()  

def display_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    return Credentials.display_credentials()  

def main():
    print("Hello welcome to password locker,what is your name?")
    user_name = input()

    print(f"Hello {user_name}.what would you like to do?")
    print('\n')

    while True:
        print("Use these short code:nc - new credentials,li - log in")
        validation_short_code = input().lower()
        if validation_short_code == 'nc':
            print("New account")
            print("_"*20)
            print("Username")
            login_username = input()
            print("Password")
            password = input()

            save_user(create_user(login_username,password))
            print('\n')
            print(f"Account for {login_username} created.proceed to login")
            print('\n')

        elif validation_short_code == 'li':
            print("Enter your user name")
            login_username = input()
            print("Enter your password")
            password = input()

            validated_password = user_validate(login_username,password)
            if validated_password == password:
                print("You have successfully logged in")
            else:
                print("Invalid username and password try again")

    else:
         print("Invalid option,please use the short code")

if __name__ == '__main__':
  main()