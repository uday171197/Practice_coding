from abc import ABC
from utils import Address

class Atm(object):
    """_summary_

    Args:
        object (_type_): _description_
    """    
    def __init__(self,atmid) -> None:
        self._atmid = atmid
        self._address = Address()
        
    def authenticateUser(self):
        pass
    
    def makeTransaction(self):
        pass
    
class Bank(object):
    def __init__(self,name,bankCode) -> None:
        self._name = name
        self._bankCode = bankCode
        
    def getBankCode(self):
        return self._bankCode
    
    def addAtm(self):
        pass
    
class Printer:
    def printRecept(self):
        pass
    
class CardReader():
    def readCard(self):
        pass
    
class Screen:
    def showMessage(self,message):
        pass
    
    def getInput(self):
        pass
    
class Keyboard:
    def getInput(self):
        pass
    
class CashDepositer:
    def __init__(self) -> None:
        pass
    
    def dispense_cash(self, amount):
        None

    def can_dispense_cash(self):
        None
        

class DepositeSlot(ABC):
    def __init__(self) -> None:
        self._totalAmount = 0.0
        
    def getTotalAmount(slef):
        return self._totalAmount
    
class CheckDepositeSlot(DepositeSlot):
    def getcheckedAmount(self):
        pass
    
    
class cassDepositeSlot(DepositeSlot):
    def getCashDepositeBill(self):
        pass
    
    
    

    
    
    