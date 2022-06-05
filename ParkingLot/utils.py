
from ctypes import addressof
import email
from enum import Enum
import enum
from unicodedata import name


class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE , MOTORBIKE, ELECTRIC = 1,2,3,4,5
        
class VehicalType(Enum):
    CAR, TRUCK,ELECTRIC,VAN,MOTORBIKE = 1,2,3,4,5
    
class TicketParkingStatus(Enum):
    ACTIVE, PAID, LOST = 1,2,3

class AccountStatus(Enum):
    ACTIVE, CLOSED, BLOCKLIST,CANCELED = 1,2,3,4
    
    
class Location:
    def __init__(self,streetAddress,city,state,pincode,country) -> None:
        self.__streetAddress = streetAddress
        self.__city = city
        self.__state = state
        self.__pincode = pincode
        self.__country = country
        
class Person:
    def __init__(self,name,address,email,phone) -> None:
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone