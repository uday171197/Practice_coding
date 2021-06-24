class Rectange():
    def __init__(self,width,height):
        self.width=width
        self.height=height
        
        
    def Area(self):
        return self.height*self.width
    
    def __str__(self):
        return 'Rectangle has width = {} and Height = {}'.format(self.width,self.height)
    
    def __repr__(self):
        return 'Rectangle has width = {} and Height = {}'.format(self.width,self.height)
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other,Rectange):
            return self.width == other.width and self.height == other.height
        else:
            return False
    def __lt__(self, other: object) -> bool:
        if isinstance(other,Rectange):
            return self.Area() < other.Area()
        else:
            return NotImplemented
        
    def __gt__(self, other: object) -> bool:
        if isinstance(other,Rectange):
            return self.Area() > other.Area()
        else:
            return NotImplemented
    

r = Rectange(10,20)
r.height
r.width
r.Area()
r
str(r)
r2 = Rectange(10,20)
r1 = Rectange(12,20)
# r is not r1
r1==r2
r1<r2


'''
Implementing getter and setter method in class. getter method is used 
to fetch the value of the class nad setter method is used to set the value of
class using some validations.
'''

class Rectange():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,width):
        if width < 0:
            raise ValueError('value should be positive')
        else:
            self._width = width

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,height):
        if height < 0:
            raise ValueError('value should be positive')
        else:
            self._height = height

r = Rectange(-10,10)
r.width = 10


