# Write a program to create a child class
# Teacher that will inherit the properties from the parent class staff

class Staff:
    def __init__(self, firstname, lastname, id, age):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.age = age

    def display_info(self):
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Id Number: {self.id}")
        print(f"Age: {self.age}")

class Teacher(Staff):
    def __init__(self, firstname, lastname, id, age, subject):
        super().__init__(firstname, lastname, id, age)
        self.subject = subject

    def display_info(self):
        super() .display_info()
        print(f"Subject taught: {self.subject}")

tr1 = Teacher("John", "Kamau", "S1982", 50, "Mathematics & Physics")
tr2 = Teacher("Paul", "Nyang'au'", "J7284", 45, "Kiswahili")
tr3 = Teacher("Kevin", "Kirunge", "U4311", 39, "Geography")
tr4 = Teacher("Grace", "Macharia", "L8779", 29, "Business")


print("Teacher 1 information:")
tr1.display_info()
print("\nTeacher 2 information:")
tr2.display_info()
print("\nTeacher 3 information:")
tr3.display_info()
print("\nTeacher 4 information:")
tr4.display_info()
        