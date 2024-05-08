#practice1

n=int(input("enter the number: "))
sum=0
i=0

while(i<=n):
    sum=sum+i
    i=i+1
    
print("Total of first n numbers: ",sum)


#practice2

num=int(input("enter the number: "))
fact=1

for i in range(1,num+1):
    fact*=i

print("factorial = ", fact)
