def isGreater(a,b):
    if(a > b):
        print(a, "is greater")
    elif(a == b):
        print("Both are Equals")
    else:
        print(b, "is greater")


a = 3
b = 3
isGreater(a,b)


def isSmallest(a,b):
    pass
    if(a > b):
     return b,"is Smallest"
    else:
     return (a,"is Smallest")
    
ans = isSmallest(3,2)
print(ans)