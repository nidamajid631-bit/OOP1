class Apple:
    name="red"
apple1=Apple()
apple2=Apple()
print(apple2.name)
class  Student:
    name="Ali Hassan"
    rollno=345
s1=Student()#object is created here!
print(s1.name)#(instance)
print("Roll no. is:",s1.rollno)
#example of self
class Dog:
    def __init__(self, name, breed):#self is the current object and name and breed are the parameters to pass! 
        self.name = name      # belongs to this dog
        self.breed = breed    # belongs to this dog
        print(self.name,self.breed)
    def speak(self):
        print(f"{self.name} is a {self.breed} and says woof!")
    def show_name(self):
        print(f"My name is Nida.")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("bull","Husky")
dog1.speak()
dog2.speak()
dog1.show_name()
#init function is a constructor it is not need to call as the objects are made it is called automatically
class Cat:
    def __init__(self, name):
        self.name=name
        print(self.name)
        #object attribute name.
cat1=Cat("nida")
cat2=Cat("Ali")
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        print(self.brand,self.model)
car1=Car("Mercedes","1111")
car2=Car("Honda","45f2")
class Student:
    name="nida"
    roll_number=356
    def display(self):
        return f"name is:{self.name},roll number is :{self.roll_number }"
        #point to be NOTED!
s1=Student()
s1.display()
print(s1.name)
class Book:
   def __init__(self, title, author):
       self.title = title
       self.author = author
       print(f"Book '{self.title}' by {self.author} has been added.")

b1 = Book("World War 3", "Paulo Cohelo")
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        print(f"Area is :{self.length*self.width}")
    def parameter(self):
        return f"Parameter is :{2*(self.length+self.width)}"

r1=Rectangle(2,3)
print(r1.parameter())
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print("your salary:",self.name,self.salary)
   
    def give_rise(self, amount):
        
        self.salary+=(amount/100)*self.salary   
        return f"Updated salary is:{int(self.salary)}"
e1=Employee("Nida",50000)
print(e1.give_rise(25))
class Circle:#you can also import math at once above the class!
    def __init__(self,radius):
        self.radius=radius
        print("Radius is:",self.radius)
    def area(self):
        import math
        return f"AREA of Circle:{round(math.pi *(self.radius)**2,2)}"
    def circumference(self):
        import math
        return f"Circumference of Circle:{int(2*math.pi*self.radius)}"
c1=Circle(10)
print(c1.area(),c1.circumference())
class BankAccount:
    def __init__(self,owner,balance):
      self.owner=owner
      self.balance=balance
      print("Owner is:",self.owner)
      print("Balance is:",self.balance)

    def deposit(self,amount):
      self.balance+=amount
      return f"Deposited amount:{amount}.Now the amount is:{self.balance}"
    def withdraw(self,amount):
        
        if amount>self.balance :
            print("insufficient balance")
        elif  self.balance>=0:
            self.balance-=amount 
            return f"withdrawn amount: {amount}. The balance is :{self.balance}"
             
b1=BankAccount("Nida",10000)
print(b1.deposit(2000))
print(b1.withdraw(2900))
#INHERITANCE
#inheriting the functionalities from parent class
class Polygon:
    def __init__(self,sides):
        self.sides=sides
        print(f"the side is:{self.sides}")
    def area(self, length):
        self.length=length
        return f"area is:{length*length}"
class Square(Polygon):
    pass 
s1=Square(4)
print(s1.area(5))
p1=Polygon(7)
print(p1.area(8))
#what if we inherit the same functionalities but differ at the same time!
class Polygon:
    def __init__(self,sides):
        self.sides=sides
        print(f"the side is:{self.sides}")
    def area(self, length):
        self.length=length
        return f"area is:{length*length}"
class Square(Polygon):
    pass 
class Triangle(Polygon):
    def area(self,base,height):# Here the method is overridden!
       return f"Area of triangle is:{int(0.5*base*height)}"
t1=Triangle(4)
print(t1.area(4,8))
class Myclass:
    def __init__(self, name, rollno):#init is a constructor doesnt return anything!
        self.name=name
        self.rollno=rollno
        print (f"{self.name} {int(self.rollno)}")
# m1=Myclass("Nida",44)
class Lecture(Myclass):
    def __init__(self, name, field, rollno):
        self.field=field
        super().__init__( name, rollno)
      

    def sub(self,subject):
        self.rollno=subject
        return f"Subject is:{self.rollno}"
m1=Myclass("Nida",12)
l1=Lecture("Amna","CS",14)
print(l1.name,l1.field,l1.rollno)
print(l1.sub("English"))
print(l1.sub("Math"))
class Person:
    name="Nida"
    age=19
class Student(Person):
    grade="A"
    def display(self):
        print(f"Name:{self.name} Age:{self.age} Grade:{self.grade}")
s1=Student()
s1.display()
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
class Car(Vehicle):
    def __init__(self ,brand, model, year):
        self.year=year
        super().__init__(brand, model, )
        print("Car created:",self.year)

c1=Car("Mercedes", "B11", 2003)
print(c1.brand)
#MULTIPLE INHERITANCE
class Human:
    def __init__(self,age,name):
        self.age=age
        self.name=name
class Dancer:
    def __init__(self, style):
        self.style=style
class Student(Human,Dancer):
    def __init__(self, age, name, style):#for inheriting one class we use super to use same constructor but for two classes we use their names!
        Human.__init__(self, age, name)
        Dancer.__init__(self,style)
   
j1=Student(20,"Nida","top")
print(j1.name)
#need more practice
class Principal:
    def __init__(self, staff, progress ):
        self.staff=staff
        self.progress=progress
class VicePrincipal:
    def monitor(self):
        print("The Vice Principle Monitors!")
class Teacher(Principal,VicePrincipal):
     def __init__(self,staff,progress,field):
         self.field=field
         Principal.__init__(self,staff,progress)

t1=Teacher("Room1","Positive","Science")
t1.monitor()
print(t1.staff)
print(t1.progress)
print(t1.field)
class Task:
    def __init__(self, title, assignedto,deadline,status="Pending"):
        self.title=title
        self.assignedto=assignedto
        self.deadline=deadline
        self.status=status
    def display(self):
        print("Print the title:",self.title)
        print("Assign to:",self.assignedto)
        print("Deadline is:",self.deadline)
        print("Status is:",self.status)
        print('-'*30)

class User:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def display(self):
        print(f"User:{self.name} , Role:{self.role}")

class Admin(User):
    def __init__(self, name):
        User.__init__(self,name,"Admin")
    def add_task(self,task_list,title,assingnedto,deadline):
        self.task_list=task_list
        new_task=Task(title,assingnedto,deadline)# it calls the constructor of Task class
        task_list.append(new_task)
        print(f'\n Task{} added ')
