#4. Write a Python script to check if a given key already exists in a dictionary.

d1={1:10,2:20,3:30,4:40,5:50}
d=input("Enter new key=")
if d in d1:
    print("key is already exist")
else:
    print("key is not exist")
