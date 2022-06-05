from utils import *
from abc import ABC
from parkingdisplay import ParkingDisplayBoard


class ParkingFloor(ABC):
    def __init__(self,name) -> None:
        self.__name = name
        self.__handicapped_spots = {}
        self.__large_spot = {}
        self.__electric_spot = {}
        self.__compact_spot = {}
        self.__motorbike_spot = {}
        self.__info_portals = {}
        self.__free_handicapped_spot_count = {'free_spot': 0}
        self.__free_compact_spot_count = {'free_spot': 0}
        self.__free_large_spot_count = {'free_spot': 0}
        self.__free_motorbike_spot_count = {'free_spot': 0}
        self.__free_electric_spot_count = {'free_spot': 0}
        self.__display_board = ParkingDisplayBoard()
        
    def add_parking_spot(self,spot):
        swicher = {
            ParkingSpotType.HANDICAPPED : self.__handicapped_spots.put(spot.get_number(), spot)
        }
    
    
a = {}
a.values('a','c')
        
        