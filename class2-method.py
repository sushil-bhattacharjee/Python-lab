class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'global-on.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Anik', 'Brahmachari', 100000)
emp_2 = Employee('Sushil', 'Bhattacharjee', 250000)

#

emp_2.fullname()
emp_1.fullname()

print(Employee.fullname(emp_1))
print(emp_1.pay)
print(emp_1.email)
print()
print(Employee.fullname(emp_2))
print(emp_2.pay)
print(emp_2.email)
