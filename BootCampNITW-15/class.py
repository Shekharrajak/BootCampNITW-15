class Employee(object):
    def __init__ (self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept
    def getDetails(self):
        print("Hello ;this is %s ,salary %s and dept is : %s"%(self.name,self.salary,self.dept))
spr= Employee("Shekahr Prasad Rajak","1000000","CSE")
spr.getDetails()

class parttimeemp (Employee):
    def __init__(self,name,dept)
        self.name=name
        self.dept=dept




