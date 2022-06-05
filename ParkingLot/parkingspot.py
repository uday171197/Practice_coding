
from utils import *
from abc import ABC


class ParkingSpot(ABC):
    def __init__(self,number, parking_spot_type) -> None:
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__Free = True
        self.__vehicle = None
        
    
    def is_free(self):
        return self.__Free
    
    def is_assigned(self,vehicle):
        self.__vehicle = vehicle
        self.free = False
        
    def is_remove(self):
        self.__Free = True
        
    
class Handicapped(ParkingSpot):
    def __init__(self, number, parking_spot_type = ParkingSpotType.HANDICAPPED) -> None:
        super().__init__(number, parking_spot_type)
        
class Compact(ParkingSpot):
    def __init__(self, number, parking_spot_type = ParkingSpotType.COMPACT) -> None:
        super().__init__(number, parking_spot_type)
        
        
class Electric(ParkingSpot):
    def __init__(self, number, parking_spot_type = ParkingSpotType.ELECTRIC) -> None:
        super().__init__(number, parking_spot_type)
        
        
class Large(ParkingSpot):
    def __init__(self, number, parking_spot_type = ParkingSpotType.LARGE) -> None:
        super().__init__(number, parking_spot_type)
        
class Motorbike(ParkingSpot):
    def __init__(self, number, parking_spot_type = ParkingSpotType.MOTORBIKE) -> None:
        super().__init__(number, parking_spot_type)
    
    
        
