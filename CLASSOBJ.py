# class Employee:
#     second_name = "Juma"
#     raise_amnt = 2.0
#     def __init__(self, name, gender, salary):
#         self.name = name
#         self.gender = gender
#         self.salary = salary
#         self.email = name + "@gmail.com"
#
#     def full_name(self):
#         return self.name
#     def salary_increase(self):
#         self.salary = int(self.salary * 1.05)
#
#         # @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
# #INHERITANCE
# class Developer(Employee):
#     def __init__(self, name, gender, salary, program_lang):
#         super().__init__(name, gender, salary)     #tells the child class what arquments it has borrowed from the parent class
#         self.program_lang = program_lang
# developer1 =  Developer("Cynthia", "female", 60000, "Python")
# developer2 = Developer("Marj", "male", 60000, "Javascript")
#
# class Receptionist(Employee):
#     def __init__(self, name, gender, salary, age):
#         super().__init__(name, gender, salary)
#         self.age = age
# receptionist1 = Receptionist("Anna", "female", 60000, "23")
# receptionist2 = Receptionist("Ainsha", "male", 60000, "32")
#
# empl1 = Employee("Sifa", "Female", 30000)
# empl2 = Employee("Shannon", "Male", 20000)
# empl3 = Employee("Ashley", "Female", 78000)
#
# print(empl1.name)
# print(empl1.email)
# print(empl2.name)
# print(empl2.email)
# print(empl3.name)
# print(empl3.email)
# print(f"{empl1.name} is a {empl1.gender} and she earns {empl1.salary}")
# print(f"{empl2.name} is a {empl2.gender} and she earns {empl2.salary}")
# print(f"{empl3.name} is a {empl3.gender} and she earns {empl3.salary}")
#
# print(empl1.full_name())
# print(empl1.salary)
# empl1.salary_increase()
# print(empl1.salary)
# print(empl2.salary)
# empl2.salary_increase()
# print(empl2.salary)
#
# Employee.raise_amnt = 3
# print(empl1.raise_amnt)
# print(Employee.raise_amnt)
#
# empl3.salary_increase()
# print(empl3.salary)
#
# Employee.set_raise_amount(2.0)
# print(Employee.raise_amount)
# print(empl1.raise_amount)
#
#
#
# # create a student program and capture their first names,
# # last name, and marks of 2 subjects then create two instances
# # from it. Perform addition of the two subject using a method
#
# class Students:
#     def __init__(self, first_name, last_name, subject1_marks, subject2_marks):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.subject1_marks = subject1_marks
#         self.subject2_marks = subject2_marks
#     # self.total = eng + math
#     def total_marks(self):
#         return self.subject1_marks + self.subject2_marks
#     def average_marks(self):
#         return self.subject1_marks / self.subject2_marks
#
#
# student1 = Students("Marrie", "Smith", 65, 90)
# student2 = Students("Abby", "Kamauu", 50, 90)
# student3 = Students("Mitchelle", "Roberts", 46, 78)
# student4 = Students("Rianna", "Fenty", 80,76)
#
# print(f"{student1.first_name} {student1.last_name} maths score is {student1.subject1_marks} physics is {student1.subject2_marks} thus total marks is {student1.total_marks()}")
# print(f"{student2.first_name} {student2.last_name} maths score is {student2.subject1_marks} physics is {student2.subject2_marks} thus total marks is {student1.total_marks()} ")
#
# print(student1.total_marks())
# print(student1.average_marks())
# print(student2.total_marks())
# print(student2.average_marks())

# create a class of a person and implement three child
# classes from the parent class person then display them

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Child classes
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

# Creating instances of the child classes
student = Student("Alice", 20, "S1234")
teacher = Teacher("Bob", 35, "Math")
employee = Employee("Charlie", 30, "E5678")

# Displaying the information for each instance
print("Student Information:")
student.display_info()
print("\nTeacher Information:")
teacher.display_info()
print("\nEmployee Information:")
employee.display_info()



