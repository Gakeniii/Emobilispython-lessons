#A function is a block of code that runs when called upon
def my_function():
    print("Hello World!")
my_function()

# OBJECT ORIENTED PROGRAM (OOP)
# A function that is associated with an object is called a method
class my_person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def my_func(self):
        print("Hello" +  self.name + "!")

p1 = my_person("Sifa", 20)

p1.my_func( )