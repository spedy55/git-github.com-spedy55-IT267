class Rectangle:
    def __init__(self) -> None:
        self.width = 0
        self.length = 0
        self.a = 0

    def get_data(self):
        self.width = float(input("Enter width: "))
        self.length = float(input("Enter length: "))

    def compute_area(self):
        self.a = self.width * self.length

    def print_area(self):
        print(f"Rectangle Area : {self.a}")

rec_obj = Rectangle()
rec_obj.get_data()
rec_obj.compute_area()
rec_obj.print_area()