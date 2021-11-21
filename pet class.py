#write a class called Pet and define the attributes
#write the necessary accessors and mutators.
#display result


class Pet:
    __name=''
    __animal_type=''
    __age=''
    
    def __init__(self):
        self.__name=''
        self.__animal_type=''
        self.__age=''

    def set_name(self,name):
        self.__name=name
        
    def set_animal_type(self,animal_type):
        self.__animal_type=animal_type

    def set_age(self,age):
        self.__age=age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

print('Here is the data that you entered:')

x=Pet()
name=input('Pet name: ')
x.set_name(name)
animal_type=input('Animal type: ')
x.set_animal_type(animal_type)
age=input('Age of pet: ')
x.set_age(age)




