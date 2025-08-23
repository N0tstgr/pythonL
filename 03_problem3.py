class Employee:
    def __init__(self, name,  salary):
        self.name = name
        self.salary = salary
        


    def show(self):
        print(f"this is the name {self.name} of the Employee and here is his salary {self.salary}")

        def increment(self, percent):
            self.salary  = self.salary * (percent/100)

e = Employee("zordan", 400000)
e.show()
