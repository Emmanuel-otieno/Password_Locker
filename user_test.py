import unittest
from user import User

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.new_account = User("Emmanuel","Facebook","072593","sakoemmanuel4@gmail.com") #created account object

    def test_init(self):
        """
        test_init is to test if the objects are initialized properly
        """ 
        self.assertEqual(self.new_account.user_name,"Emmanuel")
        self.assertEqual(self.new_account.account_name,"Facebook")
        self.assertEqual(self.new_account.password,"072593")
        self.assertEqual(self.new_account.email,"sakoemmanuel4@gmail.com")