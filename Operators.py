# ARITHMETIC OPERATORS
# Addition
a = 5
b = 7
print(a + b)
# Subtraction
print(b-a)
print(a-b)
# Multiplication
print(a*b)
# Division
print(a/b)
# Percentage
print(a%b)
# Powers
# print(a**b)  =Means a to the power of b i.e 5 to the power of 7

# ASSIGNMENT OPERATORS
c = 10
c = (c + 5)
c+=5   #assignment variable
print(c)

d = 7
d-=4
print(d)

p = 8
p = p * 2  # p*=2  --- is the assignment variable
print(p)

b = 4
b/=2
print(b)

# COMPARISON OPERATOR - ==,!=,<=,=>,<,>
# Equal to (==)
# a = 10
# b = 20
# print(a==b)
# # Not equal to (!=)
# a!=b
# print(a!=b)
# print(a<b)
# print(a<=b)
# print(a>b)
# print(a>=b)

#LOGICAL OPERATORS
# and, or, not
d = 4
f = 8
# print((d>f) and (d<f))
# print((d<f) and (d>f))
# print((d>f) and (d==f)) #the whole response is either true or false
# print((d<f) and (d==f))
#
# print((d>f) or (d<f)) #one response is true
# print((d<f) or (d>f))
# print((d>f) or (d==f))

print(not((d>f) and (d<f)))   #not 4 is greater than 8 but 4 is less than 8
print(not((d>f) or (d<f)))

# IDENTITY OPERATOR== is, is not
x = 6
y = 3
print(x is y)
print(x is not y)
print(type(x) is type(y))

# MEMBERSHIP OPERATOR
a = 'Welcome to Full Stack Development'
print('Stuck' in a)
print('Full' not in a)

# create a user input function that will
# take two integers and compare them to
# determine which one is greater
name = input("What is your name? ")
age1 = input("Enter your age ")
name2 = input("What is your name? ")
age2 = input("Enter your age ")
print(not((age1<age2) and (age1>age2)))
print(not((age1>age2) and (age1==age2)))




