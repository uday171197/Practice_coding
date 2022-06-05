import utils

class  Account:
    def __init__(self, userName,password,status = utils.AccountStatus.ACTIVE) -> None:
        self.__userName = userName
        self.__password = password
        self.__status = status
        
    def reset_password(self):
        pass
    
class Admin(Account):
    def __init__(self, userName, password, status=utils.AccountStatus.ACTIVE) -> None:
        super().__init__(userName, password, status)
        
    def add_parking_floor(self):
        pass
    
    def add_parking_slot(self):
        pass
    
    def add_paking_attendent(self):
        pass
    
    def add_charges(self):
        pass
    
    def add_intrance_panel(self):
        pass
    
    def add_exit_panel(self):
        pass
    
class PaekingAttendent(Account):
    def __init__(self, userName, password, status=utils.AccountStatus.ACTIVE) -> None:
        super().__init__(userName, password, status)
        
    def process_ticket(self):
        pass
    
    
    
    