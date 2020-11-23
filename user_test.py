import unittest
from user import User

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = User("Emmanuel","Facebook","072593","sakoemmanuel4@gmail.com") #created account object

    def test_init(self):
        """
        test if the objects are initialized properly
        """ 
        self.assertEqual(self.new_account.user_name,"Emmanuel")
        self.assertEqual(self.new_account.account_name,"Facebook")
        self.assertEqual(self.new_account.password,"072593")
        self.assertEqual(self.new_account.email,"sakoemmanuel4@gmail.com")


    def test_save_account(self):
        """
        """
        self.new_account.save_account()
        self.assertEqual(len(User.account_list),1)

    
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """  
        User.account_list = []  



    def test_save_multiple_account(self):
        """
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        """
        self.new_account.save_account()
        test_account =User("sakoemma","Insta","939687","sako@ins.com")
        test_account.save_account()
        self.assertEqual(len(User.account_list),2)

    def test_delete_account(self):
        """
        test_delete_account to test if we can remove an account from our account list
        """
        self.new_account.save_account()
        test_account = User("sakoemma","Insta","939687","sako@ins.com")
        test_account.save_account()

        self.new_account.delete_account()# deleting the account object
        self.assertEqual(len(User.account_list),1)





    def test_find_account_by_account_name(self):
        """
        test to check if we can find an account by account_name and display information
        """  
        self.new_account.save_account()
        test_account = User("sakoemma","Insta","939687","sako@ins.com")
        test_account.save_account()  

        found_account = User.find_by_name("Insta")
        self.assertEqual(found_account.email,test_account.email)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = User("zelly","linkedin","00000","zelly@lk.com") # new account
        test_account.save_account()

        account_exists = User.account_exist("00000")

        self.assertTrue(account_exists)

    
        

if __name__ == "__main__":
    unittest.main()