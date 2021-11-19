class User:
    def __init__(self, name, amount):
        self.name = name
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
    def make_withdrawal(self, amount):
        self.amount -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}.")
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
richard = User("Richard", 5000)
richard.make_deposit(10)
richard.make_deposit(15)
richard.make_deposit(20)
richard.make_withdrawal(30)
richard.display_user_balance()
matt = User("Matt", 5000)
matt.make_deposit(15)
matt.make_deposit(40)
matt.make_withdrawal(30)
matt.make_withdrawal(35)
matt.display_user_balance()
luke = User("Luke", 5000)
luke.make_deposit(40)
luke.make_withdrawal(20)
luke.make_withdrawal(30)
luke.make_withdrawal(25)
luke.display_user_balance()

luke.transfer_money(400, richard)