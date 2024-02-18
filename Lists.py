my_list = [588,893,239,208,23,378,789,109283]
print(my_list)
print(my_list[0])
print((my_list)[3])
print(my_list[7])
print(my_list[2:7]) #============PRINTS IN A RANGE
my_list[7] = 688
print(my_list)
my_list[4] = 500
print(my_list)
my_list[2:7] = 400,300,700,799,788,699
print(my_list)
print(len(my_list))    #================= SHOWS THE LENGTH
my_list.append(743)
print(my_list)
my_list.insert(0,700)
print(my_list)
my_list.insert(2, 400)
my_list.insert(1, 200)
print(my_list)
my_list.extend([588,893,239,208])
print(my_list)
my_list.remove(688)
print(my_list)
del my_list[5:15] #===============HOW TO REMOVE SEVERAL VALUES AT ONCE FROM THE LIST
print(my_list)
my_list.clear()
print(my_list)

my_list2 = [23,23,45,77,76,21,12,3,12]
max(my_list2)     #========Gives the highest value in the list
print(max(my_list2))
min(my_list2)     #========Gives the minimum value in the list
print(min(my_list2))

sum(my_list2)           #GIVES THE SUM
print(sum(my_list2))

#AVERAGE OF THE ENTIRE LIST
print(sum(my_list2)/len(my_list2))

if 23 in my_list2:
    print("Yes is it present")
else:
    print("No present")


# EXERCISE
# Create a list of 5students names then search one of the names
# if present

students = ["John", "Smith", "Aliya", "Hypatia", "Adia"]
print(students.remove("Aliya"))
if "Aliya" in students:
    print("Aliya is present")
else:
    print("Aliya is not present")

