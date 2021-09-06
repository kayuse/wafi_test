import unittest
from user import User
from transfer_service import TransferService


class UserTest(unittest.TestCase):

    def test_add_user(self):
        user = User(firstname='Kayode', lastname='Olaniyi',
                    email='kaysolaniyi@gmail.com', phone='08148380710')
        self.assertEqual(user.firstname, 'Kayode')

    def test_credit_account(self):

        user = User(firstname='Kayode', lastname='Olaniyi',
                    email='kaysolaniyi@gmail.com', phone='08148380710')
        user.credit(2000)
        self.assertEqual(user.get_balance(), 20)

    def test_debit_account(self):
        user = User(firstname='Kayode', lastname='Olaniyi',
                    email='kaysolaniyi@gmail.com', phone='08148380710')
        response = user.debit(1000)
        self.assertEqual(response, False)
        user.credit(2000)
        response = user.debit(1000)
        self.assertEqual(response, True)
        self.assertEqual(user.get_balance(), 10)


class TransferServiceTest(unittest.TestCase):

    def test_transfer(self):
        user1 = User(firstname='Kayode', lastname='Olaniyi',
                     email='kaysolaniyi@gmail.com', phone='08148380710')
        user2 = User(firstname='Victor', lastname='Umunze',
                     email='victor@gmail.com', phone='081111111')
        user1.credit(1000)
        transfer_service = TransferService(user1, user2, 500)
        response = transfer_service.process()
        self.assertEqual(user1.get_balance(), 5)
        self.assertEqual(user2.get_balance(), 5)


if __name__ == '__main__':
    unittest.main()
