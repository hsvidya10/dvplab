def b2d(n):
    return int(n,2)
def o2h(n):
    return hex(int(n,8))
bnum=input("enter binary no")
dnum=b2d(bnum)
print("Decimal number is=",dnum)
onum=input("enter octal number")
hnum=o2h(onum)
print("hexadecimal number is=",hnum)