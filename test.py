class MyClass:
    x = 5
    y = 6

# made a class

p1 = MyClass()
p2 = MyClass()

print(type(p1))

#objects from the class

print(p1.x,p2.y)

# printed value from object in class

del p1

# deleted object p1

try:
    print(p1.x, p2.y)
except:
    print(p2.x, p2.x)

#make sure p1 is deleted



#All classes have a built-in method called __init__(), which is always executed 
#when the class is being initiated.

class Person:
    def __init__(self, name, age):  #__init__() is called every time a class is being used to create a new object
        self.name = name
        self.age = age

p1 = Person("Dylan", 16)

print(p1.name)
print(p1.age)