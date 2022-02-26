from abc import ABC
from utils import TransactionStatus
from datetime import datetime

class Transaction(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """    
    def __init__(self,trancactionId) -> None:
        self._trancactionId = trancactionId
        self._status = TransactionStatus
        self._created_date = datetime.now()
        
    def saveTrancation():
        pass
    
class BalanceInquary(Transaction):
    def __init__(self, accountId) -> None:
        self._accountId =accountId
    
    def getAccount(self):
        pass
    
class Withdraw(Transaction):
    def __init__(self, amount) -> None:
        self._amount =amount
    
    def getAccount(self):
        return self._amount
    
class Transfer(Transaction):
    def __init__(self,destinationAccountNumber,sourceAccountNumber,amount) -> None:
        self._destinationAccountNumber = destinationAccountNumber
        self._sourceAccountNumber = sourceAccountNumber
        self_amount = amount
        
class Deposite(Transaction):
    def __init__(self,amount) -> None:
        self._amount = amount
        
    def getAmount(self):
        return self._amount
    
class CheckDeposite(Deposite):
    def __init__(self,checkNumber,bankCode) -> None:
        self._checkNumber = checkNumber
        self._bankCode = bankCode
        
class CashDeposite(Deposite):
    def __init__(self,cashDepositeLImit) -> None:
        self._cashDepositeLImit = cashDepositeLImit
    
    
    
    