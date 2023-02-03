#printing even numbers
i=2
while i<=20:
    if(i%2==0):
        print(i)
    i=i+1

#checking given number is float or integer 
# logic 1
i=10
if(type(i)==int):
    print("given number is integer")
else:
    print("given number is float")

#logic 2
n=2.0
if(isinstance(n,int)==True):
    print("given number is integer")
else:
    print("given number is float")

#logic 3

n=10.3
result=n-int(n)
if(result==0):
    print("given number is integer")
else:
    print("given number is float")
 

#playing with numbers program   
m=int(input("enter your range to play game:"))
import random
n=random.randrange(1,m)
guess=int(input("enter your guess:"))
while n!=guess:
    if(guess<n):
        print("your guess is too low ")
        guess=int(input("enter your guess:"))
    elif(guess>n):
        print("your guess is too high ")
        guess=int(input("enter your guess:"))
    else:
        break
print("you guessed the right")


#checking if conditions
n=int(input("Enter your Number: "))
if(n==500):
    print("Given Number is 500")
else:
    print("Given Number  is not 500")


#checking largest number
n1,n2=int(input("Enter Your FIrst Number: ")),int(input("Enter Your Second Number: "))
if(n1>n2):
    print(n1,"is the biggest one ")
else:
    print(n2,"is the biggest one ")



#largest of 3 numbers
n1,n2,n3=int(input("Enter Your FIrst Number: ")),int(input("Enter Your Second Number: ")),int(input("Enter Your Third Number: "))
if(n1>n2 and n1>n3):
    print(n1,"is the biggest one ")
elif(n2>n1 and n2>n3):
    print(n2,"is the biggest one ")
else:
    print(n3,"is the biggest one ")

    
#positive or negative numbers
n=int(input("Enter Your Number: "))
if(n>0):
    if(n%2==0):
        print("Given Number is Even-positive ")
    else:
        print("Given Number is odd-positive ")
else:
    if(n%2==0):
        print("Given Number is Even-Negitive ")
    else:
        print("Given Number is odd-Negative ")


#while loop
i=1
while i<=10:
    print(i)
    i=i+1



