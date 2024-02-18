my_dictionary = {
    "Name": "Sifa",
    "Gender": "Female",
    "Status": "Single"
}
print(my_dictionary)

my_dictionary = dict(
    Name="Sifa",
    Gender="Female",
    Status="Single"
)
print(my_dictionary)

print(my_dictionary['Gender'])     #print specific dictionary value  WITHOUT GET USE ()

print(my_dictionary.get('Status'))   #prints a specific dictionary value   WITH GET USE []
print(my_dictionary['Name'])
my_dictionary['Status'] = 'Complicated'       #edits a value in the dictionary
print(my_dictionary)
my_dictionary['BirthDate'] = '1970'          #adds a key and a value  ALWAYS USE []
print(my_dictionary)
my_dictionary['LastName'] ='Gakeni'
print(my_dictionary)

my_dictionary2 = my_dictionary.copy()
print(my_dictionary)
print(len(my_dictionary2))
my_dictionary.pop('LastName')       #removes a dictionary
print(my_dictionary)
del my_dictionary2['Status']
print(my_dictionary2)
my_dictionary.clear()
print(my_dictionary)

if 'Name' in my_dictionary2:my_dictionary2
else:
    print("Name is not in dictionary")

for value in my_dictionary2:        #shows the values individually
    print(my_dictionary2[value])

for key in my_dictionary2:
    print(key)

for key, value in my_dictionary.items():
    print(key, value)

#EXERCISE
# create a dictionary that captures shop items and their prices
# then search through the dictionary for any other item; add one more
# element in the dictionary

my_dictionary1 = {'Bread': 'KSH 60',
                  'soda': 40,
                  'Chewing gums': 20,
                  'Gummy bears': 210,
                  'Lip balm': 300}
print(my_dictionary1)
print(my_dictionary1.get('Gummy bears'))
my_dictionary1['Juice2L'] = 'KSH 300'
print(my_dictionary1)

del my_dictionary1['Juice2L']

if 'Juice2L' in my_dictionary1:
    print("Juice2L is in dictionary")
else:
    print("Juice2L is not in dictionary")











