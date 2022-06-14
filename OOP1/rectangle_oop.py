class Rectangle:
    def __init__(self,width,length) -> None:
        self.w = width
        self.l = length
        self.a = 0

    def get_data(self):
        pass

    def compute_area(self):
        self.a = self.w * self.l

    def print_area(self):
        print(f"Rectangle Area : {self.a}")

rec_obj = Rectangle(4.5,8)
rec_obj.compute_area()
rec_obj.print_area()