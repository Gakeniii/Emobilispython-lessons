set1 = {1,2,3,4,5,6,7}
print(set1)
var1 = 2
if var1 in set1:
    print(var1)
var2 = 6
if var2 in set1:
    print(var2)

set1.add(9)
print(set1)
set1.update([54,63,365,63])
print(set1)
set1.discard(5)
print(set1)