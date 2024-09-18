num=int(input("enter a number"))
val=str(num)
rev=val[::-1]
if(val==rev):
    print("the num",num,"is polindrome")
else:
    print("the num",num,"is not a polindrome")
for i in range (10):
    if(val.count(str(i))>0):
        print(str(i),"appears",val.count(str(i)),"times")