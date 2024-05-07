#practice1
a=int(input("enter a number:"))
if (a%2==0):
    print(a,"number is even");
            
else:
    print(a,"number is odd")


#practice2
x=int(input("First num: "))
b=int(input("second num: "))
c=int(input("third num: "))

if(x>b):
    if(x>c):
        print(x, "is greater")
    elif(c>x):
        print(c,"is greater")
elif(b>x):
    if(b>c):
        print(b,"is greater")
    elif(c>b):
        print(c, "is greater")
else:
    print("numbers are equal")

#practice3
y=int(input("enter the number:"))
if(y%7==0):
    print(y, "is multiple of 7")
else:
    print(y, "is not multiple of 7")