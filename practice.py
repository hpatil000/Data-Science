# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for marks in self.marks:
#             sum = sum+marks
#         avg = sum/len(self.marks)
#         return avg



# s1 = Student("Harshita", [90, 80, 85])
# print(s1.name, s1.marks)
# print("average Marks:", s1.get_avg())


# s2 = Student("Shreya", [99, 98, 97])
# print(s2.name, s2.marks)
# print("average Marks:", s2.get_avg())



class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

        print("welcome to your account", )

    def credit(self, add_money):
        # add_money = int(input("Enter ammount of money to add"))
        self.balance = self.balance + add_money
        return self.balance
    
    def debit(self, deduct_amount):
        # deduct_amount = int(input("Enter amount of money to withdraw"))
        if self.balance > deduct_amount:
            self.balance = self.balance - deduct_amount
        else:
            print("Insufficient balance")
        return self.balance
    
    def current_balance(self):
        return self.balance


acc1 = Account(10000, "abcde12345")
print("your balance is:",acc1.balance,"\nYour account number" ,acc1.account)
acc1.credit(5000)
print("your balance is ", acc1.balance)
acc1.debit(2000)
print("your balance is ", acc1.balance)
       