myArray = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']

reverse=myArray[::-1]

if myArray == reverse:
    print("Symmetric")
else:
    print("Asymmetric")    