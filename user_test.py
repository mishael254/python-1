import unittest
from user import User

class TestUser(unittest.TestCase):
     def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki","james@ms.com")


     def test_init(self): 
        '''
        test_init test case to test if the object is initialized properly
        '''
     def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user_account
        '''
        

        self.assertEqual(self.new_user.first_name,"James") 
        self.assertEqual(self.new_user.last_name,"Muriuki")
        
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.contact_list),1)#here we check the length of the contact list to confirm an addition has been made

     def tearDown(self):
            """
            this is a teardown method that basically cleans up after each test case has been run
            """
            User.user_account = []

     def test_save_multiple_users(self):
          """
          the test_save_multiple_contact is to check whether we can save more than one contact
          objects to our contact list

          """
          self.new_user.save_user()
          test_user = User("Test","user","testuser@yahoo.com") #new contact
          test_user.save_user()
          self.assertEqual(len(User.user_account),2)
          #we want now to make a test to delete the contact saved
     def test_delete_user(self):
           """
          this test_delete_contact is to test if we can delete a contact from our contact list
           """
           self.new_user.save_user()
           test_user = User("Test","user","testuser@yahoo.com")#new contact
           test_user.save_user()

           self.new_user.delete_user()#deleting a new contact object
           self.assertEqual(len(User.user_account),1)

     def test_find_user_by_password(self):
          """
          test to find whether we can find a contact by number and display information
          """
          self.new_user.save_user()
          test_user = User("Test","user","testuser@yahoo.com")
          test_user.save_user()

          found_user = User.find_by_email("testUser@yahoo.com")
          self.assertEqual(found_user.password,test_user.password)

     def test_user_exists(self):
          """
          test to check if we can return a boolean if the contact does not exist
          """
          self.new_user.save_user()
          test_user = User("Test","user","testuser@yahoo.com")
          test_user.save_user()
         
          user_exists = User.user_exist("0711223344")

          self.assertTrue(user_exists)

     def test_display_all_(self):
          """
          a test that returns a list of all contacts saved
          """
          self.assertEqual(User.display_user(),User.user_account)

          
          
           
     
     
     
       
if __name__ == '__main__':
    unittest.main()