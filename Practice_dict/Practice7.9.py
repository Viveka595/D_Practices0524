#9. Write a Python program to remove duplicates(based on values) from Dictionary.

d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6:25}

c=[]

for i in d.values():
    if i in c:
        
    else:
        c.append(i)
        
        
print("After removing duplicates=",c)
