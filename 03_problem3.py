class Employee:
    salary = 344
    increment = 90
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary *(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100



e = Employee()
# print(e.salaryAfterIncrement) 
e.salaryAfterIncrement = 653
print(e.increment)


##visit it again that is not clear