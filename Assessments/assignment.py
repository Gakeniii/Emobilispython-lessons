# fruits
# name ,price and colors
# create a method "i love eating it costs and it is healthy/"
# create 5 objects

class Fruits:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

fruit1 = Fruits('Kiwi', 300, 'Furry green')
fruit2 = Fruits('Banana', 50, 'Dusty yellow')
fruit3 = Fruits('Pineapple', 120, 'Yellow orange')
fruit4 = Fruits('Custard apple', 40, 'Olive green')
fruit5 = Fruits('Dragonfruit', 790, 'Deep pink')

print(f"I love eating {fruit1.name}, it costs {fruit1.price}, and it is {fruit1.color} in color.")