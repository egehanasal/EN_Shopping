from finance import Finance


class Employee:

    id_number = 1000
    number_of_employees = 0
    employees = list()
    old_employees = list()

    def __init__(self, name):
        self.name = name
        Employee.update()
        self.employees.append(self)
        self.salary = 2500
        Finance.budget -= self.salary
        Finance.report("Employee", self.salary, "expense")
        self.id_number = Employee.id_number

    @classmethod
    def update(cls):
        cls.number_of_employees += 1
        cls.id_number += 1

    def give_raise(self):
        self.salary += 200
        raise_ = 200
        Finance.budget -= raise_
        Finance.report("Employee", raise_, "expense")

    def __str__(self):
        return "Employee name: " + self.name + "\nid: " \
                + str(self.id_number) + "\nSalary: " + str(self.salary) + "\n"

    def fire(self):
        Employee.employees.remove(self)
        Employee.old_employees.append(self)

    __repr__ = __str__


