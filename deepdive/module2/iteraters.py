class Cubes:
    def __init__(self,lenght) -> None:
        self.length = lenght
        self.i = 0
        
    def __len__(self):
        return self.length
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i**3
            self.i += 1
            return result
        
    def __iter__(self):
        return self
    
    
c1 = Cubes(5)

for i in c1:
    print(i)
    

class Citys:
    def __init__(self) -> None:
        self.city = list('ABCD')
        
    def __len__(self):
        return len(self.city)
    

class Itercity:
    def __init__(self,city_obj):
        self.city_obj = city_obj
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.city_obj):
            raise StopIteration
        else:
            result = self.city_obj.city[self.index]
            self.index += 1
            return result
        
        
city = Citys()

iter = Itercity(city)

for i in iter:
    print(i)



# creating iterables 




class Citys:
    def __init__(self) -> None:
        self.city = list('ABCD')
        
    def __len__(self):
        return len(self.city)
    
    def __iter__(self):
        return self.Itercity(self)
    
    def __getitem__(self,s):
        return self.city[s]
    
    
    class Itercity:
        def __init__(self,city_obj):
            self.city_obj = city_obj
            self.index = 0
            
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.index >= len(self.city_obj):
                raise StopIteration
            else:
                result = self.city_obj.city[self.index]
                self.index += 1
                return result
        
        
city = Citys()

for i in city:
    print(i)

city[0]


# creating circular iterators

class CircularIterators:
    def __init__(self,data) -> None:
        self.data = data
        self.i = 0
        
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.data[self.i%len(self.data)]
        self.i += 1
        return result
    

it = CircularIterators('ABC')

for i in range(10):
    next(it)
    
    
    
    
# Lazy iterators
import math
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
        self._area = None
        
    @property
    def radius(self):
        return self._radius
        
    @radius.setter
    def radius(self,r):
        self._radius = r
        self._area = None
        
    @property
    def area(self):
        if self._area is None:
            print('calculating area')
            self._area = math.pi * (self.radius ** 2)
        return self._area
    
    
        
        
cir = Circle(5)
cir.radius

cir.radius = 10
cir.area

cir.radius = 11





