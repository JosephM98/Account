import datetime

class Account():
    count = 0 #class or static variable
    def __init__(self, first_name , last_name, amount):
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount
        Account.count += 1
        self.customer_id = Account.count
        self.activities = []
        
        
    def deposit(self, amount):
        self.amount += amount
        activity = (datetime.datetime.now(), amount, "Deposit")
        self.activities.append(activity)
         
    def withdraw(self, amount):
        self.amount -= amount
        activity = (datetime.datetime.now(), amount, "Withdraw")
        self.activities.append(activity)
        
        
    def print_information(self):
        print(self.first_name[0] + " " + self.last_name + ": $" + str(self.amount))
        
        
da = Account("David", "Ake", 9.75)
gs = Account("Gionna", "Smith", 119.75)
ra = Account("Reuben", "Alvarez", 52.11)
aa = Account("Andy", "Norman", 500)
ra.withdraw(20.25)
da.deposit(18.18)


ra.print_information()
da.print_information()


aa.deposit(1000)
aa.withdraw(125)
aa.deposit(1000)
aa.withdraw(55)
aa.deposit(1200)
aa.withdraw(105)
aa.print_information()
print(aa.activities)


#Print activities
for a in aa.activities:
    print(a)
     
