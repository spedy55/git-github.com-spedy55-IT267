#THIS FILE INSIDE BACK PACKAGE
#CALL MODULE
from bank.customer import Customer
from bank.account import Account

cus1 = Customer()
cus1.new_customer()

cus1_acc = Account()
cus1_acc.open_account(cus1.name,'Saving','11501150',500)

print('==== Open Bank Account Detail ====')
print(cus1.cus_info())
print(cus1_acc.displayer_balance())
#print(cus1.cus_info())