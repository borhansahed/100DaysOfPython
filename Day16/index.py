import os

a = int(input("enter any thing "))
# print(os.path)

match a:
    case 0:
        
        print("i am fine")
    case 4 if(4 % 2 == 0):
        print(a, " is even ")
    case _ if a > 50 and a < 100:
        print("greater than 50")
    case _ if a < 50:
        print("lower than 50")
    case _:
        print(a)
       
