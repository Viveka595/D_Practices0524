#14. Write a Python program to match key values in two dictionaries. 
#Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
#Expected output: key1: 1 is present in both x and y

d={'key1':1,'key2':3,'key3':2}
d2={'key1':1,'key2':2}

for i in d:
    for j in d2:
        if i==j:
            if d[i]==d2[j]:
                print(i ,' is presnt in bath x amd y')

