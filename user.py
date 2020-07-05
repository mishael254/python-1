class User:
    """
    a class that generates a new user password account after providing a username and a password
    """
    user_account = []# create an empty user_account

    def save_user(self):
        """
        new method to save the users username and password
        """
        User.user_account.append(self)

    def delete_user(self):
        """
        a new method to delete users account
        """
        User.user_account.remove(self)

    def __init__ (self,username,password):
        self.username = username
        self.password = password


        @classmethod
        def find_by_password(cls,password):
          """
          a method that takes in a password and returns an account that matches that password
          arguments:=> 1 password ;this is a login password to search for an acount
          (2); returns the account  information for the found password



          """
          for user in cls.user_account:
              if user.password == password:
                   return user

    @classmethod 
    def user_exist(cls,password):
        '''
        Method that checks if a user exists from the user_account.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_account:
          if user.password == password:
              return True
        return False

    @classmethod
    def display_user(cls):
       """
       method that returns a user_account
       """
       return cls.user_account









