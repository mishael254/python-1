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







