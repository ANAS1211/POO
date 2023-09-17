import inspect

class Person:
#next is a docstring, that will be displayed
# via __doc__ magic method
#Basic class for modelisation"""
    def __init__(self):
        print("Calling constructor for modelisation")
        self.name="Nobody"

# The destructor :
# just to show, should never be re-defined !
def __del__(self):
    print("Calling destructor of class Person")
    
def __str__(self):
    s="My name is {}".format(self.name)
    return(s)

def get_name(self):
    return(self.name)
#class ends here

def main():
    person=Person()
    print(person)
    # just to show __doc__ usage
    print("Class description: {}".format(person.__doc__))
    print("playing with inspect")
    for x in inspect.getmembers(person):
        print(x)
    
if __name__=="__main__":
    main()
    
