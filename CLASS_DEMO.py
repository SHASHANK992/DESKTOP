class employee:
    empcount=0

    def __init__(self, name, salary, enrollment, da):
        self.name = ' '
        self.salary = 0
        self.enrollment = ' '
        self.da = 0
        if self.name != "null":
            employee.empcount+=1

    def displaycount(self):
        print("%d" %employee.empcount)

    def details(self):
        print("NAME:", self.name)
        print("SALARY:", self.salary)
        print("ENROLLMENT NUMBER:", self.enrollment)
        print("DEARNESS ALLOWANCE:", self.da)

    def details_input(self):
        self.name = input("ENTER EMPLOYEE NAME:")
        self.salary = input("ENTER EMPLOYEE SALARY:")
        self.enrollment = input("ENTER EMPLOYEE ENROLLMENT:")
        self.da = input("ENTER EMPLOYEE DEARNESS ALLOWANCE:")


f1 = employee(0,0,0,0)
f1.details_input()
f1.displaycount()
f1.details()


