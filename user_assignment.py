class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def transfer_money(self, other_user, amount):
        pass

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance} ")


user1 = User("Don Brown", "don@python.com")
user2 = User("Sarah Brown", "sarah@python.com")
user3 = User("Chris Brown", "chris@python.com")
# print(user1.name)
# print(user2.name)

user1.make_deposit(400)
user1.make_deposit(300)
user1.make_deposit(200)
user1.make_withdrawal(350)

user2.make_deposit(800)
user2.make_deposit(700)
user2.make_withdrawal(300)
user2.make_withdrawal(200)

user3.make_deposit(800)
user3.make_withdrawal(200)
user3.make_withdrawal(300)
user3.make_withdrawal(200)

user1.display_user_balance()
user2.display_user_balance()
user3.display_user_balance()