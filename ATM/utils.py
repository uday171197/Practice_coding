from enum import Enum


class  TrasactionType(Enum):
        """_summary_

        Args:
            Enum (_type_): _description_
        """        
        balancInquary,withdraw,cashDeposite,transfer,CheckDeposite = 1,2,3,4,5
        
class TransactionStatus(Enum):
        Success, Failure, Blocked,Nill = 1,2,3,4
        
class CustomerStatus(Enum):
        Active,Block, Banned,Closed, Archive = 1,2,3,4,5
        
class Address:
    def __init__(self,streetAddress,city,state, country, pin) -> None:
        self._streetAddress = streetAddress,
        self._city = city,
        self._state= state,
        self._country = country,
        self._pin = pin
        
        


        