import numbers
from unicodedata import name


class Account:
    def __init__(self) -> None:
        self.type = 'Saving'
        self.number = ''
        self.balance = 0

    def open_account(self,name:str,type:str,number:str,balance:int=100):
        self.name = name
        self.type = type
        self.number = number
        self.balance = balance

    def displayer_balance(self):
        return f'{self.name} account balance = {self.balance} baht'