class JuiceOrder:
    def __init__(self,menu:str,size:str="R",price:int=0):
        self.menu = menu.upper()
        self.size = size.upper()
        self.price = price

    def check_menu(self):
        menu_dic = {
            "OJ" : 25,
            "AJ" : 25,
            "WJ" : 30,
            "PJ" : 30
        }
        if self.menu in menu_dic:
            self.price = menu_dic.get(self.menu)
    
    def compute_price(self):
        if self.size == "L":
            self.price += 5
        else:
            self.price

    def display_order(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu} ({self.size} * {self.price}) => {self.price}'

if __name__ == "__main__":
    order1 = JuiceOrder('WJ','L')
    order2 = JuiceOrder('OJ')
    order3 = JuiceOrder('PJ','L')
    print(order1.display_order())
    print(order2.display_order())
    print(order3.display_order())