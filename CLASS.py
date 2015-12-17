class employee:
    empcount=0

    def __init__(self, name, salary, enrollment, da):
        self.name = " "
        self.salary = 0
        self.enrollment = " "
        self.da = 0
        if self.name != "null":
            employee.empcount += 1


    def displaycount(self):
        print("%d" %employee.empcount)

    def details(self):
        print("NAME:", self.name)
        print("SALARY:", self.salary)
        print("ENROLLMENT:", self.enrollment)
        print("DEARNESS ALLOWANCE:", self.da)

    def details_input(self):
        self.name = input("ENTER THE NAME OF EMPLOYEE:")
        self.salary = input("ENTER THE SALARY OF THE EMPLOYEE:")
        self.enrollment = input("ENTER THE ENROLLMENT NUMBER:")
        self.da = input("ENTER THE DEARNESS ALLOWANCE:")


f1 = employee(0,0,0,0)
f1.details_input()
f1.displaycount()
f1.details()




