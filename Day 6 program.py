# exception handling

a=int(input("enter your numerator:"))
b=int(input("enter your denominator:"))
try:
    print(a/b)
except Exception as e:
    print("please note that a number cannot be divided by zero",e)
finally:
    print("bye")


# exception handling example
a=10
try:
    b=int(input("enter the number:"))
    print("resource open")
    print(a/b)
except ZeroDivisionError as e:
    print("please note a number cant be divided by zero",e)
except ValueError as e:
    print("invalid input",e)
except Exception as e:
    print("other error",e)
finally:
    print("Resource closed")



#else block in exception handling
x=int(input("enter your number:"))
if x%2!=0:
    raise Exception("x shoulb be even number")
else:
    print("x is even number ..correct")



# oops concepts
class computer:
    def config(self):
        print("yes")
lenovo=computer()
lenovo.config()

dell=computer()
dell.config()

# constructor
class employee:
    def __init__(self,name,id):
        self.id=id
        self.name=name        
    def display(self):
        print("Id:%d\nName:%s"%(self.id,self.name))
emp1=employee("mani",143)
emp2=employee("pujitha",143)

emp1.display()
emp2.display()


#variiable in class and method variiable
class computer():
    a=10                                     #class variable
    b=20
    print("class variable inside class ",a)
    def config(self):                         #config is a method in class 
        c=100                                 # c is a method variable
        print("yes")
        print("instance access",self.b)      # to access an variable of class in method we need to use self. keyword
lenovo=computer()                            #creating an object of class computer,object name lenovo
print(lenovo.a)
print(lenovo.a+lenovo.b)
dell=computer()
print("dell",dell.a)                        # accessing class variable
lenovo.config()                             # accessing config method