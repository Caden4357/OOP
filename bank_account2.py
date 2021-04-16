class User: 
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
        self.account = BankAccount(int_rate = 0.02)

    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    def withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self
    def display_user_info(self):
        self.account.display_user_info()
    def yield_interest(self):
        self.account.yield_interest()
        return self

class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print("insufficient funds $5.00 fee being charged to your account")
            self.balance -= amount + 5
        else:
            self.balance -= amount
        return self
    def display_user_info(self):
        print(f"Balance is: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
        

caden = User("Caden Wilcox", "wilcox4357@gmail.com")
caden.deposit(100).withdrawal(50).withdrawal(100).yield_interest().display_user_info()
