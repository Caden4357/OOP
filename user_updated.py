class User:       #making a class naming it user
    def __init__(self, username, email_address):   
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    #adding a deposit method 
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    #adding withdrawal method
    def make_withdrawal(self, withdrawal):
        if self.account_balance - withdrawal < 0:
            print("Not enough funds") 
        else:
            self.account_balance -= withdrawal
        return self


    #Transfer money method
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name}, Balance: ${self.account_balance}")
        print(f"{other_user.name}, Balance: ${other_user.account_balance}")
        return self 

    #adding display user balance
    def display_user_balance(self):
        print(f"{self.name}, Balance:${self.account_balance}")
        return self
caden = User('Caden Wilcox', 'wilcox4357@gmail.com')
alex = User('Alex Smith', 'alexSmith@gmail.com')
monty = User('Monty Python', 'Knights@neep.com')
#Here Caden is making 3 deposits a withdrawal and showing balance 
caden.make_deposit(300).make_deposit(60).make_deposit(100).make_withdrawal(200).display_user_balance()
#Here we have alex making 2 deposits and 2 withdrawals then his balance is displayed
alex.make_deposit(500).make_withdrawal(300).make_deposit(100).make_withdrawal(400).display_user_balance()
#adding to montys account
monty.make_deposit(1000).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()
#transfering $100 from caden to
caden.transfer_money(monty, 100)


