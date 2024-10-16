def b2d (n):
    return int(n,2)
def o2h(n):
    return hex(int(n,8))
bnum=input("enter binary number")
dnum=b2d(bnum)
print("Decimal number=",dnum)
onum=input("enter octal number")
hnum=o2h(onum)
print("hexa decimal =",hnum)

