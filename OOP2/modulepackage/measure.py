class Measure:
    def __init__(self,num) -> None:
        self.num = num

    def inch_cm(self):
        return f'{self.num * 2.54:,.2F}'

    def cm_inch(self):
        return f'{self.num / 2.54:,.2F}'

if __name__ == '__main__':
    m1 = Measure(12.5)
    m2 = Measure(100)
    print(m1.inch_cm())
    print(m2.cm_inch())