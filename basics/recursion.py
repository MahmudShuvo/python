#practice 1
#sum of n numbers of natural numbers
def calc_sum(n):
    if(n==0):
        return 0
    
    return calc_sum (n-1)+n

sum= calc_sum(10)
print(sum)

#practice 2
#print all elements in a list

def print_elements(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_elements(list,idx+1)

fruits=["mango",'Licchi',"Apple"]
print_elements(fruits)
