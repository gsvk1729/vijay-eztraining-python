#lambda function
l=[1,2,3]
r=map(lambda x:2*x,l)
print(list(r))

res=map(lambda n:pow(n,2),l)
print(list(res))

name="Akhil  10000"
(lambda name:print(name))(name)

#problem
l=[]
for i in range(1,16):
    if(i%2==0):
        l.append(i)
squ=map(lambda a:pow(a,1/2),l)
print(list(squ))



#abstraction

import abc from ABC
class abstractdemo(ABC):
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()


#single inheritance

class parent:
    def display(self):
        print("parent class")
        
class child(parent):
    def show(self):
        print("derived class")

c=child()
c.display()
c.show()

class a:
    n=30
        
class b(a):
    def calc(self):
        c=self.n+70
        print(c)

b().calc()

#multiple inheritance

class mom():
    def mdisplay(self):
        print("mom class")
class dad():
    def ddisplay(self):
        print("dad class")
class child(mom,dad):
    def cdisplay(self):
        print("child class")
        
a=child()
a.mdisplay()
a.ddisplay()
a.cdisplay()   

#multilevel inheritance

class grandparent():
    def display(self):
        print("grand parent class")
class parent(grandparent):
    def pdisplay(self):
        print("parent class")
class child(parent):
    def cdisplay(self):
        print("child class")
        
a=child()
a.display()
a.pdisplay()
a.cdisplay()   

#hierarchial inhertiance

class parent():
    def pdisplay(self):
        print("parent class")
class child1(parent):
    def c1display(self):
        print("child 1 class")
class child2(parent):
    def c2display(self):
        print("child 2 class")
        
a=child1()
a.pdisplay()
a.c1display()
'''a.c2display() --you will get an error with this as child 1 has no right to access child 2 property 🤪'''  
b=child2()
b.c2display()
b.pdisplay()

#hybrid inheritance

class parent():
    def pdisplay(self):
        print("parent class")
class kid1(parent):
    def k1display(self):
        print("kid 1 class")
class kid2(parent):
    def k2display(self):
        print("kid 2 class")
class c1(kid1):
    def c1display(self):
        print("child 1 class")
class c2(kid1):
    def c2display(self):
        print("child 2 class")
class cc1(kid2):
    def cc1display(self):
        print("c child 1 class")
class cc2(kid2):
    def cc2display(self):
        print("c child 1 class")
c1().c1display()
c1().k1display()
c1().pdisplay()
cc1().cc1display()
cc1().k2display()

