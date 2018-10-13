def print_bottlebeers(n):
    if(n==0):
        print("no beer bottle left, go to the shop to buy some!")
    else:
        print(str(n)+" beer bottles still on the wall, go get one!")
        print_bottlebeers(n-1)

print_bottlebeers(10)

s1 = "this is string 1"
print("s1={}, s1.size={}, s1.__class__={}".format(s1, len(s1), s1.__class__))

s2 = str("this is string 22")
print("s2={}, s2.size={}, s2.__class__={}".format(s2, len(s2), s2.__class__))

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_entry(self):
        return "title={}, author={}".format(self.title, self.author)


b1 = Book("small red", "David")
print("b1 object's attribute: "+str(dir(b1)))
print(b1.title + ", " + b1.author)

print(b1.get_entry)

print("99bottles.jet.py; this module's module_name is:"+__name__)

import jet_first_module

print("module:jet_first_module's attributes=" + str(dir(jet_first_module)))
print("module:jet_first_module's class=" + str(jet_first_module.__class__))
print("jet_first_module.B2's attributes=" + str(dir(jet_first_module.B2)))

#this reference of current module
import sys
current_module = sys.modules[__name__]
print("current_module's class=" + str(current_module.__class__))
print("current_module's attributes=" + str(dir(current_module)))


#get names of attributes for current module: dir()
print("current module's name={}, current module's attributes={}".format(str(__name__), str(dir())))

print("class str's base class=" + str(str.__bases__))
print("class object's base class=" + str(object.__bases__))

print("class str's ancestors="+str(str.__mro__))

print("object's subclass="+str(object.__subclasses__()))
