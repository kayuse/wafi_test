class TransferService:
    errors = []

    def __init__(self, initiator, recepient, amount):
        self.initiator = initiator
        self.recepient = recepient
        self.amount = amount

    def process(self):
        if self.initiator.debit(self.amount):
            self.recepient.credit(self.amount)
            return True
        else:
            self.errors.append(self.initiator.get_errors())
            return False
        self.errors.append('Could Not complete Transfer')
        return False

    def get_errors(self):
        return self.errors
