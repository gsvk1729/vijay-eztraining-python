#list
l=[4,2,3,7]
print(l)
print(l.index(3))

print(l[:3])

l.insert(1,22)
print(l)

l.remove(22)
print(l)

l.pop(3)
print(l)

l.sort()
print(l)

l.reverse()
print(l)


#displaying elements of the list
l=[1,2,3,4]
for i in range(len(l)):
    print(l[i])

print()

# using member ship operators 
for j in l:
    print(j)



#printing even numbers in a list
l=[1,2,3,4]
for i in l:
    if(i%2==0):
        print(i)

#taking input from the user
size=int(input("size:"))
l=[]
for i in range(size):
    ele=int(input("element:"))
    l.append(ele)

print(l)

for j in l:
    if(j%2==0):
        print(j)


#list example problem
size=int(input("size:"))
l=[]
for i in range(size):
    ele=int(input("element:"))
    l.append(ele)
print(l)
prod=1

for j in l:
    prod=prod*j

sum=0

for k in l:
    sum=sum+k

if(prod<750):
    print("prod=",prod)
else:
    print("sum=",sum)

#method 2

n=list(map(int,input("enter ").split()))
print(n)

prod=1

for j in l:
    prod=prod*j

sum=0

for k in l:
    sum=sum+k

if(prod<750):
    print("prod=",prod)
else:
    print("sum=",sum)


#list comprehension
number=[elements for elements in "Great Afternoon"]
print(number)

# can create a list using existing list
l=['vijay',"shiva","sai satish","farukh"]
s=[]
for i in l:
    if "ai" in i:
        s.append(i)
print(s)
l1=[1,2,3,4,5,6]
l2=[i for i in l1 if (i<5)]
print(l2)


#sets and their operations
s={1}
print(type(s))
s.add(2)
print(s)
s.update([25,35])
print(s)
s.discard(2)
print(s)
s.remove(25)
print(s)

s={1,2,3}
s1={1,4,5}
print("union=",s1|s)
print("intersection=",s&s1)
print("s-s1=",s-s1)

# symmetrical difference
print("symmetrical difference=",s^s1)

#tuple
t=(4,5,6,4,2,3,4)
print(type(t))
print("count of 4 is",t.count(4))
print("index of 4 is",t.index(4))


#dictionary
d={1:"one",2:"two"}
print(d)
print(type(d))
print(d.keys())
print(d.values())
print(d.items())
print(d[1])

#or get function
print(d.get(1))

d.update({"c":89})
print(d)
d.pop(1)
print(d)
d.popitem()
print(d)
d.setdefault("angle",700)
print(d)
d.setdefault(1,"changed")
print(d)
d.setdefault("vijay",)
print(d)