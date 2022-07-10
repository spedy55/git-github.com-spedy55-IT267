from bank import Bank

class Abank(Bank):
    def __init__(self,bankname:str,loanamount:int,loanyear:int,loanrate:float,interest:float=0,monthlypay:float=0) -> None:
        self.bankname = bankname
        self.__loanamount = loanamount
        self.__loanyear = loanyear
        self.__loanrate = loanrate
        self.interest = interest
        self.monthlypay = monthlypay
    
    @property
    def loanamount(self):
        return self.__loanamount
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value

    @property
    def loanyear(self):
        return self.__loanyear
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value * 12

    @property
    def loanrate(self):
        return self.__loanrate
    @loanrate.setter
    def loanrate(self,value):
        self.__loanrate = value

    def flat_rate(self):
        self.interest = self.__loanamount * ( self.__loanrate / 100) * self.__loanyear
        self.monthlypay = ( self.__loanamount + self.interest ) / self.__loanyear

    def display_interest(self):
        print(f'Loan : {self.loanamount}')
        print(f'Rate : {self.loanrate}%')
        print('----------')
        print(f'Interest : {self.interest} baht')
        print(f'Monthly Repayment : {self.monthlypay} baht')

loan = Abank('SCB',100000,2,3)
loan.display_interest()