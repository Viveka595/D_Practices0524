#11. Write a Python program to combine two dictionary adding values for common keys.
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3={}
for i in d2:
    print(d2[i])
    for j in d1:
        if j==i:
            d3[j]=d1[j]+d2[i]
        else:
            d3[i]=d2[i]
            d3[j]=d1[j]


print(d3)    
