from cgi import print_exception
from unicodedata import name


class Item:
    def __init__(self,name:str,price:float,quantity:int) -> None:
        assert price >=1 ,f"Price should more than or equal to 1"
        assert quantity >=1 ,f"Quantity should more than or equl to 1"
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculate_total_price(self):
        return self.price * self.quantity

    def __del__(self):
        print(f'Object Destroy')

if __name__ == "__main__":
    item1 = Item("Cup",25,2)
    item2 = Item("Cone",10,3)
    print(f"------- Total Price -------")
    print(f"{item1.name}: {item1.calculate_total_price()}")
    print(f"{item2.name}: {item2.calculate_total_price()}")
