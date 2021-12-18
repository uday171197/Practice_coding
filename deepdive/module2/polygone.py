

import math
class polygone:
    def __init__(self,edge,radius) -> None:
        self.edge = edge
        self.radius = radius
        self.vertices = edge
        self.interior_angle = (edge-2)*(180/edge)
        self.edge_length = 2*radius*math.sin(math.pi/edge)
        self.apothem = radius*math.cos(180/edge)
        self.area = 0.5 * self.apothem * self.edge_length
        self.parameter = edge * self.edge_length
        
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
        
        
        
class Polygone:
    def __init__(self,m,r) -> None:
        if m < 3:
            raise ValueError("m should be greate then 2")
        
        self.m = m
        self.r = r
        self.polygones = [polygone(i,r) for i in range(3,self.m+1)]
        
    def __len__(self):
        return self.m-2
    
    def __repr__(self) -> str:
        return f"The Polygone({self.m,self.r})"
    
    
p = Polygone(5,8)
    
for _ in p.polygones:
    print(_)
    



p1 = polygone(5,10)

p2 = polygone(5,20)

p1<p2

p1==p2



