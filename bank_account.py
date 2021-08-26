class Bank:

    def __init__(self, account: str, balance: int):
        self.account = account
        self.balance = balance

    def __repr__(self):
        return f'Account: {self.account}; Balance: {self.balance}'

    def deposit(self, num):
        self.balance = self.balance + num
        print("Deposit successfully!")

    def withdraw(self, num):
        if self.balance >= num:
            self.balance = self.balance - num
            print("Withdraw successfully!")
        else:
            print("Not having enough money!")


if __name__ == "__main__":
    jonathan = Bank('jonathan', 100)
    print(jonathan)
    jonathan.deposit(100)
    print(jonathan)
    jonathan.withdraw(50)
    print(jonathan)
    jonathan.withdraw(200)
    print(jonathan)
