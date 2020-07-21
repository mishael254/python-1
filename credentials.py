class Credentials:
    """
    Class that generates new instances of credentials
    """

    credentials_list = [] 

    def __init__(self,username_name,account_name,account_password):

      

        self.username_name = username_name
        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)  

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self) 

    @classmethod
    def display_credentials(cls):
        '''
        Method that takes in a number and returns a contact that matches that number.
        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        
        return cls.credentials_list      
    