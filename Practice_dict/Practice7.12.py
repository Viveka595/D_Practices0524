#12. Write a Python program to print a dictionary in table format.

d1 = {'a': 100, 'b': 200, 'c':300}

print('keys','--','values\n----------------')
for i in d1:
    print('  ',i,'--',d1[i])
