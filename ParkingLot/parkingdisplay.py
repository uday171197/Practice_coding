from email import message


class ParkingDisplayBoard:
    def __init__(self,id) -> None:
        self.__id = id
        self.__handicapped_free_slot = None
        self.__electric_free_slot = None
        self.__compact_free_slot = None
        self.__large_free_slot = None
        self.__motorbike_free_slot = None
        
        
    def show_empty_spot_number(self):
        message = ""
        if self.__handicapped_free_slot.is_free():
            message += 'Free Handicapped : ' + self.__handicapped_free_slot.get_number()
        else:
            message +=  "Handicapped is Full"
            
        message += "\n"
        
        message = ""
        if self.__electric_free_slot.is_free():
            message += 'Free Electric : ' + self.__electric_free_slot.get_number()
        else:
            message +=  "Electric is Full"
            
        message += "\n"
        
        message = ""
        if self.__compact_free_slot.is_free():
            message += 'Free Compact : ' + self.__compact_free_slot.get_number()
        else:
            message +=  "Compact is Full"
            
        message += "\n"
        
        message = ""
        if self.__large_free_slot.is_free():
            message += 'Free Large : ' + self.__large_free_slot.get_number()
        else:
            message +=  "Large is Full"
            
        message += "\n"
        
        message = ""
        if self.__motorbike_free_slot.is_free():
            message += 'Free Motorbike : ' + self.__motorbike_free_slot.get_number()
        else:
            message +=  "Motorbike is Full"
            
        message += "\n"
        
        print(message)
    