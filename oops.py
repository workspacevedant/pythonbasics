class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def salary(self):
        return self.salary


rohan = employee("rohan", 50000)
print(rohan.salary)
print(rohan.name)