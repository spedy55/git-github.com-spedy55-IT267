from cusorder.customer import Customer
from cusorder.order import Order

cus = Customer('Jame','Nontaburi')
ord = Order('15-06-2022','packed')

print(f'Order of {cus.name} on {ord.date} is {ord.status}')