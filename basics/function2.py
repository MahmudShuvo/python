#practice 1
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

n=int(input("enter the number you want to find factorial: "))
cal_fact(n)

#practice 2
def convert_Dollar_to_Money(Dollar):
    Money=0
    Money=Dollar*120
    print("After conversion Money =",Money)

Dollar=int(input("Dollar : "))
convert_Dollar_to_Money(Dollar)
