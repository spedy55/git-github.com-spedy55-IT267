from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self,bankname:str) -> None:
        super().__init__()
        self.bankname = bankname
        print(f'===== {self.bankname} Loan Info =====')

    @abstractmethod
    def flat_rate(self):
        pass