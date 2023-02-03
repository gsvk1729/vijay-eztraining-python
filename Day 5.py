#random module
import random as r #defining random as r
x="i love you"
print(r.sample(x,2))

# shuffle -adjust allelements randomly in list
a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)

# choice- choose a element from the batch
print(r.choice(a))
b="welcome back"
print(r.choice(b))

a=r.random() #will return random number b/w 0.0 to 1.0
print(a)     

#randint
print(r.randint(20,30)) # randint choose a random int b/w 20 to 30

#choices
a=[10,20,30,40,50]
print(r.choices(a,k=10)) # choices select elements from a randomly upto k terms note:only k is used
s="hello good day"
print(r.choices(s,k=10))

#uniform
print(r.uniform(5,10)) #returns any  random number b/w 5 to 10 including 5,10 also and returns float value

# calendar
print()
import calendar
print("Full calendar:")
print(calendar.calendar(2022))
print("Particular Month:\n")
print(calendar.month(2022,3))
# by defalut python day start with monday 
print("set first day of the week\n")
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2025,5))

#DATETIME MODULE
import datetime
a=datetime.datetime.now()
print(a)
sv=a.strftime("%y") # shorter version  of year
fv=a.strftime("%Y") # full version of year
print()
print("year short version:",sv)
print("year full version:",fv)

#Function::::::
#functin creation
def greet():
    print("Have a great day")
    print("Happy time")
greet() # function call

#without argument,without return value
def multiply():
    x=int(input("enter your first number:"))
    y=int(input("enter your second number:"))
    z=int(input("enter your third number:"))
    prod=x*y*z
    print("product is:",prod)
multiply()


#without argument,with return value
def multiply():
    x=int(input("enter your first number:"))
    y=int(input("enter your second number:"))
    z=int(input("enter your third number:"))
    prod=x*y*z
    return prod
res=multiply()
print(res)



#with argument,without return value
def multiply(n1,n2,n3):
    prod=n1*n2*n3
    print("product is:",prod)
multiply(1,2,3)
print("with user input")
def multiply(n1,n2,n3):
    prod=n1*n2*n3
    print("product is:",prod)
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
c=int(input("enter your third number:"))
multiply(a,b,c)


#with argument,with return value
def multiply(n1,n2,n3):
    prod=n1*n2*n3
    return prod  
res=multiply(1,2,3)
print(res)
print("with user input")
def multiply(n1,n2,n3):
    prod=n1*n2*n3
    return prod
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
c=int(input("enter your third number:"))
print(multiply(a,b,c))

#lemons program
def l():
    x=int(input("enter the lemons in hand:"))
    if(x>21):
        print("you have",x-21,"more lemons ")
    elif(x<21):
        print("you have to  buy",21-x, "more lemons to visit temples ")
    else:
        print("you have enough lemons to visit temple")
l()


#factors
def factors(a):
    for i in range (1,a+1):
        if(a%i==0):
            print(i)
n=int(input("enter your number:"))
factors(n)

#multiplication function
a=int(input("enter which table you want:"))
def multi(n):
    for i in range(1,11):
        print(n,"x",i,"=",i*n)
multi(a)


#sum of the diigit
a=int(input("enter your number :"))
def sum(n):
    sum=0
    while(n>0):
        b=n%10
        sum=sum+b
        n=int(n/10)
    return(sum)
x=sum(a)
print(x)


#recursive function 
def display():
    n=int(input("enter your number:"))
    if n==10:
        display()
    else:
        print("bye")
display()


#fibanoci series

n=int(input("Enter Number:"))
a=0
b=1
sum=0
count=1
while(count<=n):
    print(sum,end="")
    count+=1
    a=b
    b=sum
    sum=a+b



#neon number 
def neon():
    n=int(input("enter your number:"))
    sq=n*n
    sum=0
    while(sq!=0):
        b=sq%10
        sum=sum+b
        sq=int(sq/10)
    if (sum==n):
        print("given number is neon number")
    else:
        print("given number is not neon number")
neon()


# function return more than one value
def add_sub(x,y):
    sub=x-y
    add=x+y
    return add,sub  #in which way you are giving in return statement it will give o/p in that way
a=int(input("enter your first number:"))
b=int(input("enter your second number:"))
res1,res2=add_sub(a,b)
print(res1)
print(res2)



