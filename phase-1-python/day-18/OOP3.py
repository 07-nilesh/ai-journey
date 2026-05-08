class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def from_string(cls, emp_str):
        """Alternative Constructor: Creates an object from a hyphenated string."""
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay)) # 'cls' refers to the Employee class
    @staticmethod
    def is_workday(day):
        """Utility: Checks if a given date is a working day (Mon-Fri)."""
        # Python's weekday(): 0=Mon, 5=Sat, 6=Sun
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
emp_1 = Employee('Nilesh', 'kashyap', 50000)
emp_2 = Employee.from_string('Arya-kashyap-60000')  
print(emp_1.first)  # Output: Nilesh
print(emp_2.first)  # Output: Arya  
import datetime
my_date = datetime.date(2024, 6, 15)  # This is a Saturday
print(Employee.is_workday(my_date))  # Output: False, since it's a weekend