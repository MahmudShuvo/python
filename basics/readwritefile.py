#write
a=open("practice.txt","w")
a.write("Hi Eyeryone. \nwe are learning File I/O \nusing Java. \nI like programming in Java")
a.close()

#read and replace
with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("Java","Python")
print(new_data)

#overwrite
with open("practice.txt","w") as f:
    f.write(new_data)

#search
word="learning"
with open("practice.txt","r") as f:
    data=f.read()
    if(word in data):
        print("found")
    else:
        print("nai")

#linewise check
def check_line():
    wordd="learning"
    dataa=True
    line_no=1
    with open("practice.txt","r") as f:
        while dataa:
            dataa = f.readline()
            if(wordd in dataa):
                print(line_no)
                return
            line_no +=1
    return -1
check_line()


#create practice1 and read data one by one

d=open("practice1.txt","w")
d.write("1,2,76,84,90,101")
d.close()

with open("practice1.txt","r") as q:
    datA=q.read()
    print(datA)

    num=""
    for i in range(len(datA)):
        if(datA[i]==","):
            print(int(num))
            num=int(num)
                
            num=""
        else:
            num+=datA[i]
#another way to find total number of even numbers
count=0
with open("practice1.txt","r") as f:
    data= f.read()

    nums= data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count+=1
print(count)

        
        

