# bitwise operations
print("enter your numbers, note your numbers should be less than 15")
n1,n2=int(input("enter your first number:")),int(input("enter your second nmuber:"))
print("your two numbers are:",n1,n2)
print("output of bitwise and is", n1&n2)
print("output of bitwise or is", n1|n2)
print("output of bitwise xor is", n1^n2)
print("output of bitwise not of n1 is", ~n1)
print("output of bitwise not of n2 is", ~n2)
print("output of bitwise leftshift of n1 for 2bits is ", n1<<2)
print("output of bitwise rightshift of n1 for 2bits is ", n1>>2)


#calculations
i=int(input("enter your integer:"))
f=-(float(input("enter your float integer:")))
result=i*f
print("result is:",result)


#candy problem
sugar_candy=75
sam=float(sugar_candy/2)
sugar_candy=float((sugar_candy/2)+(sam/2))
sam=float(sam/2)
print("sugar candy sam is having:",sam)
print("sugar candy remaining:",sugar_candy)


# funny game 
print("upside triangle:\n")
print("*************")
print(" *********** ")
print("  *********  ")
print("   *******   ")
print("    *****    ")
print("     ***     ")
print("      *      ")


print()

print("my heart:\n")

print(" #        #  ")
print("#  #    #  # ")
print("#     #    # ")
print(" #        # ")
print("  #      # ")
print("   #    #  ")
print("    #  #   ")
print("      #    ")



#end sep
print("its",'a','good','day')
print("all",'is','good')

print()

print("its",'a','good','day',end='**') #In python bydefault print line ends with \n so vcursor after printing move to next line
#by using end we are saying the compiler to end   the line with ***
print("all",'is','good')               #this line accompines with day in previous line

print()

print("its",'a','good','day',sep='#')  #each string is seperated by sep instruction  

#calculations

a=(3*36.32)
a=a+56.19
a=a-10
print("final result is:",a)

# multiple input from user 

n=int(input("size:"))
a=list(map(int,input("Numbers:").split()))[:n]
print(a)

#printing name

print(chr(3125)+chr(3135)+chr(3100)+chr(3119)+chr(3149))

# product of numbers 

n=int(input("size:"))
a=list(map(int,input("Numbers:").split()))[:n]
prod=1
for i in a:
    prod=prod*i
print(prod)

#simple if

n=int(input("enter your room temperature:"))
if(n>45):
    print("weather is  hottest ")
elif(35<n<=45):
    print("weather is  hot  ")
elif(26<n<=35):
    print("weather is  moderate ")
elif(10<n<=26):
    print("weather is  cool ")
elif(0<n<=10):
    print(" weather is coolest")
else:
    print("out of database")

#swaping texti1=int(input("enter your first number"))
i2=int(input("enter your second number"))
print("before swaping")
print("n1=",i1)
print("n2=",i2)
temp=i1
i1=i2
i2=temp
print("after swaping")
print("n1=",i1)
print("n2=",i2)

#swaping without temp
a,b=input("enter your 2 numbers:").split()
print("\nBefore swaping")
print("a=",a)
print("b=",b)
a,b=b,a
print("After swaping")
print("a=",a)
print("b=",b)

#taking data from user 
print("INPUT:")
print()
a=int(input("ENTER YOUR FIRST INTEGER :"))
b=int(input("ENTER YOUR SECOND INTEGER :"))
c=int(input("ENTER YOUR THIRD INTEGER :"))
print()
d=float(input("ENTER YOUR FIRST FLOAT :"))
e=float(input("ENTER YOUR SECOND FLOAT :"))
f=float(input("ENTER YOUR THIRD FLOAT:"))
print()
g=input("ENTER YOUR FIRST STRING:")
h=input("ENTEWR YOUR SECOND STRING:")
print()
i=complex(input("ENTER YOUR COMPLEX NUMBER:"))
print()
print("OUTPUT:")
print("First Integer:",a)
print("Second Integer:",b)
print("Third Integer:",c)
print("\nFirst Float:",d)
print("Second Float:",e)
print("Third Float:",f)
print("\nFirst String:",g)
print("Second String:",h)
print("\nComplex Number:",i)




