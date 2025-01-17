from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,first_name,last_name): 
        self.first_name = first_name
        self.last_name = last_name

    @property
    def fullName(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def Salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name,salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def Salary(self):
        return self.salary
    
    def Show_Detial(self):
        print(self.fullName)
        print(self.Salary())

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name,hours,rate):
        super().__init__(first_name, last_name)    
        self.hours = hours
        self.rate = rate

    def Salary(self):
        return self.rate * self.hours
    
    def Show_Detial(self):
        print(self.fullName)
        print(self.Salary())

# Main Part Start Here 
Ali = FullTimeEmployee("Ahmed","Ali",23000)
Amna = HourlyEmployee("Amna","Javed",12,300)

Ali.Show_Detial()
print("------------")
Amna.Show_Detial()



# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return 2 * (self.width + self.height)


# rectangle = Rectangle(5, 4)


# print(rectangle.area())       
# print(rectangle.perimeter())  
