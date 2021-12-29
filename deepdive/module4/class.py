class Person:
    name = 'uday'
    abc = '12345'
    pass

import pandas 
Person.name

type(Person)

Person.x = 100
Person.__dict__

getattr(Person,"name")

getattr(Person,'abc')
getattr(Person,'x')
getattr(Person,'x1','N/A')
getattr('Hellp','1','N/A')

setattr(Person,"x1",100)

Person.x1

delattr(Person,'x1')

Person.__dict__


Person.name


'''
class and function
'''


class Person:
    language = 'Python'
    
    def my_fun():
        return f'My language is {Person.language}'
    
    
    
Person.__dict__
Person.my_fun()


# Data Attribute 

class Program:
    language = 'Python' # class variable 

Program.__dict__

Program.language

p = Program()

p.__dict__

p.language
type(Program.__dict__)

type(p.__dict__)


p.__dict__['name'] = 'uday' # instance variable

p.__dict__
# It show error because it it dont allow to change the value of the mappingproxy dictionary.
Program.__dict__['name'] = 232

# first it will check whether that variable exist in instance name space of data does nor ecist then it will 
#  search in class namespace

p.__dict__
p.language

