class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        self.update_balance()

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.update_balance()
        
    def update_balance(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """
    Docstring explaining my class:
    THis class generates checking account objects
    """
    #class variable, shared among all object instances
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
        self.update_balance()

account = Account("balance.txt")