class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
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
        

account_one = BankAccount()
account_two = BankAccount(int_rate = 0.04, balance = 12000)
account_one.deposit(300).deposit(200).deposit(600).withdrawal(500).yield_interest().display_user_info()
account_two.deposit(4000).deposit(2000).withdrawal(600).withdrawal(1000).withdrawal(4000).withdrawal(2440).yield_interest().display_user_info()

