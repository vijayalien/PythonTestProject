class Employee:
    no_of_leaves=8
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary
        print(f"The name is :{name} Salary is :{salary} Age is :{age}")

    def set_work(self, work):
        return f"The work is: {work}"


vijay=Employee("Vijay", 28, 50000)
print (vijay.no_of_leaves)
print (vijay.set_work("Tester"))

