age = 8
if age >= 18:
    print("You are old enough to join")
    print("You are expected to have an ID")
else:
    print("You are young to move out")

grade =559
if grade >= 80 and grade <= 100:
    print("You are an A material!")
elif grade >= 70 and grade <= 80:
    print("You are B material")
elif grade <= 60 and grade >=50:
    print("You are C material")
elif grade <= 50 and grade >=40:
    print("You are D material")
elif grade <= 40 and grade >=30:
    print("You are E material")
elif grade <= 20 and grade >=0:
    print("You are F material")
else:
    print("Your marks are not recorded")

# create  a system that captures the
# temperature input from user and states them as follows
# if temperature is less than 20 degrees celcius tell the person
# to put on a sweater, if the temperature is less than 30 degrees celsius
# tell the person to put on a shirt and if it's less than 40 degrees celsius
# tell the person to remove the shirt

name = input("What is your name? ")
temperature = int(input("Enter the temperature in Celsius: "))

if temperature >=0 and temperature <=20:
    print(name, "Kindly put on your Sweater")
elif temperature >=20 and temperature <=30:
    print(name, "Kindly put on your shirt")
elif temperature >=30 and temperature <=40:
    print(name, "Kindly remove your shirt")







