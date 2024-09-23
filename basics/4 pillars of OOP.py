#practice 1
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.1416*self.radius ** 2
    def parameter(self):
        return 2 * 3.1416 * self.radius

c1=Circle(21)
print(c1.area())
print(c1.parameter())

#practice 2
class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    
    def showdetails(self):
        print("role =", self.role)
        print("department =", self.department)
        print("salary =", self.salary)
    
class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT", "75000")

engg1 = Engineer("Shuvo","24")
print(engg1.name)
engg1.showdetails()

#practice 3
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1=Order("chips",20)
odr2=Order("lollypop",5)

print(odr1>odr2)

