#practice1
a=input('1st movie:')
b=input('2nd movie:')
c=input('3rd movie:')

list=[a,b,c]
print(list)

#practice1 better approach
movies=[]
movies.append(input("enter 1st:"))
movies.append(input("enter 2nd:"))
movies.append(input("enter 3rd:"))
print(movies)

#practice2

list1=[1,2,3,2,1]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):{
    print("palindrome")
}
    
else:
    print("not palindrome")

#listslicing (using length, last one include hoy nah)
