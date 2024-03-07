class factory:                                            #class

    __prize="55M"

    def __init__(self,brand,name):                        #constructor
        self.brand=brand
        self.name=name

    print(f"Prize is {__prize}.")                         #printing private member

    def show(self):
        #method to display the object details
        return (f"This car is a {self.brand} and it's named {self.name}.")                         

swift=factory("Maruti Suzuki","Swift")                    #object
print(f"Name of car : {swift.name}")                      #printing public attribute
print(f"Brand of car : {swift.brand}")                    #printing public attribute
print(f"Show Details : {swift.show()}")                   #calling method 