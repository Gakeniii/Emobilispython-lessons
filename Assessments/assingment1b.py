# Create three classes, 'Person' and 'Employee' and 'Student'
# use multiple inheritance to create a class "person"
# that inherits from both employee and student
# add attributes an methods specific to each other

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display_info(self):
        print(f"Name: {self.firstname} {self.lastname}")

class Employee(Person):
    def __init__(self, namef, namel, age, salary):
        super().__init__(namef, namel)
        self.age = age
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")

class Student(Person):
    def __init__(self, namef, namel, age, school):
        super().__init__(namef, namel)
        self.age = age
        self.school = school

    def display_info(self):
        super().display_info()
        print(f"School: {self.school}")

per1 = Employee("Sifa", "Gakeni", 20, "ksh35000")
per2 = Employee("Maria", "Chepkoriri", 24, "ksh45000")
per3 = Student("Amelia", "Njenga", 18, "STCGHS")
per4 = Student("Meena", "Shing", 34, "Ksh50000")

print("Person 1 information:")
per1.display_info()
print("\nPerson 2 information:")
per2.display_info()
print("\nPerson 3 information:")
per3.display_info()
print("\nPerson 4 information:")
per4.display_info()