from operator import attrgetter

li = [-6, -5, -4, 1, 2, 3]

s_li = sorted(li, key=abs)
print(s_li)


class Employee:
    def __init__(self, name=None, age=None, salary=None):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'Employee({self.name}, {self.age}, {self.salary})'


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

s_employees = sorted(employees, key=lambda e: e.age, reverse=True)
s_employees = sorted(employees, key=attrgetter('name'), reverse=True)
print(s_employees)
