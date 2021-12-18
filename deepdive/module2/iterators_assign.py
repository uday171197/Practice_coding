import math
class polygone:
    def __init__(self,edge,radius) -> None:
        self.edge = edge
        self.radius = radius
        self.vertices = edge
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._parameter = None
        
        
    @property
    def vertices(self):
        self.vertices = self.edge
        
    property
    def interior_angle(self):
        if self._interior_angle == None:
            self._interior_angle = (self.edge-2)*(180/self.edge)
        return self._interior_angle
        
    property
    def edge_length(self):
        if  self._edge_length == None:
            self._edge_length = 2 * self.radius*math.sin(math.pi/self.edge)
        return self._edge_length   
        
    property
    def apothem(self):
        if self._apothem == None:
            self._apothem = self.radius*math.cos(180/self.edge)
        return self._apothem
    
    property
    def area(self):
        if self._area == None:
            self._area = 0.5 * self.apothem * self.edge_length
        return self._area
    
        
    property
    def parameter(self):
        if self._parameter == None:
            self._parameter = self.edge * self.edge_length
        return self._parameter
        
    def __repr__(self) -> str:
        return f"polygone ({self.edge,self.radius})"
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other,polygone):
            if self.edge == other.edge and self.radius == other.radius:
                print('both polygone are equal')
            else:
                print('both polygone are not equal')
        else:
            print('This is not a type of polygone')
            raise NotImplemented
        
    def __gt__(self,other):
        if isinstance(other,polygone):
            if self.vertices == other.vertices:
                print('both polygone are equal ' )
            else:
                print('both polygone are not equal ')
        else:
            print('This is not a type of polygone')
            raise NotImplemented
    
    
    
class Polygones:
    def __init__(self,m,r) -> None:
        if m < 3:
            raise ValueError("m should be greate then 2")
        
        self.m = m
        self.r = r
        self.i = 3
        
    def __len__(self):
        return self.m-2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i > self.m:
            return StopIteration
        else:
            result = polygone(self.i , self.r)
            self.i +=1
            return result
        
        
        
p = Polygones(4,8)
len(p)
for i in p:
    print(i.edge)


        