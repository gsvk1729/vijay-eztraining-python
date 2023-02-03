#dict comprenshion 
d={n:n*n for n in range(1,5)}
print(d)



#calculating product price of 5 units 
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price)in old.items()}
print(new)



#with checks
real={'vijay':20,'unknown':120,'me':150}
now={name:age*5 for (name,age)in real.items()}
print(now)



#program to create a list with 8 names display a dictionary with the list along with random discounts for them
import random
l=['vijay','akhil','satish','nagendra','dora','unknown','youknow','chaitu']
d={name:random.randint(1,20) for name in l}
print(d)



# zip function in dictionary
sn=['akhil','nage','dora','satish','unknown']
stm=[490,480,499,420,150]
d={a:b for(a,b) in zip(sn,stm)}
print(d)


# example of dict comprenshion
sn=['akhil','nage','dora','satish','unknown']
tm=[490,480,499,420,150]
d={a:b for(a,b) in zip(sn,tm)}
print(d)
v=[]
for i in tm:
    p=(i/500)*100
    v.append(p)
a={c:d for (c,d) in zip(sn,v ) }
print(a)


# dict comprehension input from user and random percentage
import random
student_name=list(map(str,input("Enter Names:").split()))
mark=[]
for i in range(len(student_name)):
    a=(random.randint(300,500)/500)*100
    mark.append(a)
my_dict={x:y for (x,y) in zip(student_name,mark)}
print(my_dict)




# string:::::::

#note:we cannot use double quotes in double quotes or single quote in single quote
#to use quotes in a string we can use \
n='hi i\'am'
print(n)
# or we can simply use opposite opposite rule means we can use sigle quote with double quotes
n="hello i'am"
print(n)

# string operations

s="satya vijay krishna "
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.replace('s','S')) #replace all s to S
print(s.strip())
print(s.split())
print(s.split('a'))
print(s.center(31,'*'))
print(s.count('a'))
print(s.count('a',5,len(s))) # from 5 the of begining and till the length of element 
print(s.find('a')) # check a and returns index value of first occurance of a
print(s.find('a',5,len(s)))
print(s.index('a',7,len(s)))
print(s.isupper())  # checks whether given string all letters is of uppercase letter or not 
print(max(s)) 
print(min(s)) # space is lesser then a ,b , ......z,A,B....Z
print(s.rfind("a",0,len(s)))# checks for 'a' from  backside but counts index   from first


#mutable::::

x=20
print("x=",x,"id(X)=",id(x))
x=30
print("x=",x,"id(X)=",id(x)) #here when we update the variable the memory location of the variable is changed so it is mutable

l=[2,3,4]
print("l=",l,"id(l)=",id(l))
l.append(1729)
print("l=",l,"id(l)=",id(l)) #here id is not changed so it is inmutable

#strexample
str,char=input("enter your string:"),input("enter your character:")
if(char in str):
    print(char,'is present in ',str)
else:
    print(char,'is not present in ',str)

#palindrome
str=input("enter your string:")
a=str[::-1]
if(str==a):
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")

#finding spaces in a str without count
str=input("enter your string:")
space=0
for i in str:
    if(" "in i):
        space=space+1
if(" "in str):
    print("spaces in the string is",space)
else:
    print("string doesnt contain spaces")

#finding vowels count in string
l=['a','e','i','o','u','A','E','I','O','U']
s=input("enter your string:")
count=0
for i in s:
    for j in l:
        if(i==j):
            count+=1
print("the vowels in the string",s,"is",count)

#math module
import math
print("CEIL 12.5:",math.ceil(12.5)) #moves to nearby int higher than it 
print("FLOOR 12.5:",math.floor(12.5)) #moves to nearby int lower than it 
print("SQRT 345:",math.sqrt(345)) 
print("FACTORIAL 3:",math.factorial(3))
print("POWER 2,3:",math.pow(2,3))
print("REMAINDER 10,3",math.fmod(10,3))
a,b=divmod(10,3) # returns quotient and remainder
print(a,b)
 
