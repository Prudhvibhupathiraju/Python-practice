# class bank_account:
#     def __init__(self, owner, balance=0 ):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
    
#     def withdrawl(self, amount):
#         self.balance -= amount
#         return self.balance
    
# prudhvi = bank_account("prudhvi_1", 500)
# opt = int(input("Deposit-->1 or Withdrawl-->2\n"))
# Amount = int(input("Enter the amount\n"))
# if opt == 1:
#     print(prudhvi.deposit(Amount))
# elif opt == 2:
#     print(prudhvi.withdrawl(Amount))    

class cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        return self.color

cookie1 = cookie("green")
cookie2 = cookie("blue")

print("cookie1 is", cookie1.get_color())
print("cookie2 is ", cookie2.get_color())



print("cookie1 is", cookie1.set_color("yellow"))
print("cookie2 is ", cookie2.get_color())