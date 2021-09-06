class User:
    errors = []
    amount = 0
    def __init__(self,firstname,lastname,email,phone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
    
    def get_balance(self):
        return self.amount / 100
    
    def credit(self,amount):
        self.amount += amount

    def debit(self,amount):
        if self.amount < amount:
            self.errors.append('Insufficient funds')
            return False
        self.amount = self.amount - amount
        return True
    def get_errors(self):
        return self.errors
    