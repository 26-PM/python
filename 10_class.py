# First and the main class
class factory:                                            #class

    __prize="55M"

    def __init__(self,brand,name):                        #constructor
        self.brand=brand
        self.name=name

    print(f"Prize is {__prize}.")                         #printing private member

    def show(self):
        #method to display the object details
        return (f"This car is a {self.brand} and it's named {self.name}.") 


# Second Class
class Honda(factory):
    def __init__(self, brand, name,glasses):
        super().__init__(brand, name)
        self.glasses=glasses


# Objects and calling functions
swift=factory("Maruti Suzuki","Swift")                    #object
print(f"Name of car : {swift.name}")                      #printing public attribute
print(f"Brand of car : {swift.brand}")                    #printing public attribute
print(f"Show Details : {swift.show()}")                   #calling method 


print("\nInheritance\n")

# Inherited class "Honda" from base class "factory".
Activa=Honda("Honda","Activa",2)
print(f"Name : {Activa.name}")
print(f"Brand : {Activa.brand}")
print(f"Glasses : {Activa.glasses}")