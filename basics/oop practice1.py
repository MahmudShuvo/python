class Student:
    Average=0
    def __init__(self,name,math,phy,chem):
        self.name=name
        self.math=math
        self.phy=phy
        self.chem=chem

    def get_avg(self):
        # if (self.name== None):
        #     print("Please insert the Name")
        # elif(self.math == 0 )
        Average= (self.math + self.phy+ self.chem)/3
        print("Average : ", Average)

S1=Student("Shuvo",98,99,95)
print(S1.name)
S1.get_avg()