
from utils import Address,CustomerStatus


class Customer(object):
    def __init__(self,name,email,phoneno,address) -> None:
        self._name = name
        self._email = email
        self._phoneno = phoneno
        self._address = Address()
        self._status = CustomerStatus()
        
    def MakeTransaction(self):
        return True
    
class Account(object):
    def __init__(self,accountNumber) -> None:
        self._accountNumber = accountNumber
        self._availabeBalance = 0.0
        self._totalBalance = 0.0
        
    def getAvailabeBalance(self):
        return self._availabeBalance
        
class SavingAccount(Account):
    def __init__(self,withdrawLimit):
        self._withdrawLimit = withdrawLimit
        
class CheckingAccount(Account):
    def __init__(self,debitCardNumber):
        self._debitCardNumber = debitCardNumber
        
class Card(object):
    def __init__(self,cardNumber,customerName,expiryDate,pin) -> None:
        self._cardNumber = cardNumber
        self._customerName = customerName
        self._expiryDate = expiryDate
        self._pin = pin
        
    
        