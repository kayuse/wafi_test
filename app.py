# file to run the code
from user import User
from transfer_service import TransferService
user_a = User(firstname='Kayode', lastname='Olaniyi',
              email='kaysolaniyi@gmail.com', phone='08148380710')

user_a.credit(1000)
user_b = User(firstname='Victor', lastname='Umunze',
              email='victor@gmail.com', phone='081111111')
user_b.credit(2000)

transfer_service = TransferService(user_b, user_a, 1500)
response = transfer_service.process()
if response is True:
    print('Transer successful user a has ' + str(user_a.get_balance()) + ' and user b has ' + str(user_b.get_balance()))


another_transfer_service = TransferService(user_a, user_b, 2500)

response = another_transfer_service.process()

if response is True:
    print('Transer successful user b has ' + str(user_b.get_balance()) + ' and user a has ' + str(user_a.get_balance()))