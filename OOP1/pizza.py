class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        #ส่งคืนค่าที่สามารถพิมพ์ได้
        return f'Pizza({self.ingredients})'

    @classmethod #ถ้า method มีมากกว่า 1 อันจะใช้ @classmethod
    def margherita(cls):
        return cls(['mozzarella','tomatoes']) # cls คืออ้างอิงclassของตัวเอง

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella','tomatoes','ham'])

    @staticmethod
    #
    def size(ch): # ch คือพารามิเตอร์
        ch = ch.upper()
        if ch == 'S':
            return 'samll: 6 inches, 4 slices'
        elif ch == 'L':
            return 'Large: 14 inches, 10 slices'
        else:
            return 'Default Medium: 12 inches, 8 slices'

# create instance
my_pizza = Pizza('Cheese, Meat')
print(my_pizza)
print(my_pizza.margherita())

# static method
print('----- Static Method ------')
print(Pizza.size('L'))

# class method
print('----- Class Method ------')
print(Pizza.margherita)
print(Pizza.prosciutto)
print(my_pizza.margherita())
print(Pizza.ingredients)