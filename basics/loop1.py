#practice1

a=1
while(a<101):
    print(a);
    a=a+1
#practice2

a=100
while(a>0):
    print(a);
    a=a-1

#practice3

n=int(input('enter the number: '))
c=1
while(c<=10):
    mul=n*c;
    print(mul);
    c=c+1

#practice4

#taking the list from user
li=[]
a=int(input("enter no of elements:"))
k=1
p=0
while(k<=a):
    li.append(input("enter number"))
    k=k+1
print(li)

#printing the elements
while(p<len(li)):
    print(li[p])
    p=p+1

#practice5
tu=(1,2,3,4,5,6,7,8)
x=5
io=0

while(io<len(tu)):
    if(tu[io]==x):
        print("found at index", io,"number is", tu[io])
    io+=1
