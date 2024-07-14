#13. Write a Python program to get the top three items in a shop.
#Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#Expected Output:
#item4 55
#item1 45.5
#item3 41.3

d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
x=3
y=1
d2={}
for i in d:
    d2[i]=d[i]

print(d2)
