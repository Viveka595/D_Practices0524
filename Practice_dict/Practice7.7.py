#7. Write a Python program to remove a key from a dictionary.

d={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("dict=",d)
r=int(input("Enter key form dict to remove="))
d.pop(r)    #del d[r] #d.remove(r)      #
print("updated dict=",d)
