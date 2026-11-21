class BankAccount:
    def __init__(self, acc_no,name,acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Amount deposited",amount)

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print("Amount withdrawn",amount)
        else :
            print("Insufficient balance")

    def display(self):
        print("\n---Account Details---")
        print("Account No:",self.acc_no)
        print("Account Name:",self.name)
        print("Account Type:",self.acc_type)
        print("Balance:",self.balance)

b=BankAccount("123","Samvrutha","Savings",10000)
b.display()
b.deposit(1000)
b.withdraw(500)
b.display()