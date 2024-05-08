#practice1

#taking the list from user
li=[]
a=int(input("enter no of elements: "))
k=1
while(k<=a):
    li.append(input("enter number: "))
    k=k+1
print(li)

#printing one by one with for loop
for element in li:
    print(element)


#practice2
tu=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number you want to search: "))

for el in tu:
    if(x==tu[el]):
        print("found in", el, "index")
        break
    else:
        continue