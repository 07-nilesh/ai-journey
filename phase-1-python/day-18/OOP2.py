class Employee:
    number_of_employees = 0  # Class variable to keep track of the number of employees
    raise_amount = 1.05  # Class variable for raise amount (5% raise)
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.number_of_employees += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # Use class variable for raise amount     

emp_1 = Employee('Nilesh', 'kashyap', 50000)
print(emp_1.number_of_employees)  
emp_2 = Employee('Arya', 'kashyap', 60000)
print(Employee.number_of_employees)  
print(emp_1.__dict__)
print(Employee.__dict__)
print(emp_1.raise_amount)
emp_2.raise_amount = 1.10  # This will create an instance variable for emp_2, not affecting the class variable
print(emp_2.raise_amount)  # This will still print 1.05, as