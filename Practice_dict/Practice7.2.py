#2. Write a Python script to add an item to a dictionary
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

d={0: 10, 1: 20}
print("dict=",d)
a=input("Enter a key=")
b=input(f"Enter {a} value =")
d[a]=b
print("after insertion dic=",d)
