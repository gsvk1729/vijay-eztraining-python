q1="""what is your favourite colour?
a)green
b)blue
c)white
d)i don\'t have favourite colour
"""

q2="""
when was indian constitution was adopted?
a)26 january 1950
b)15 august 1947
c)26 november 1949
d)26 november 1950
"""
q3="""which indian song is nominated for oscar 2023
a)naatu naatu
b)ma ma mahesha
c)ponakalu loading
d)jai baalayya 
"""

q4="""5!=
a)5
b)20
c)120
d)240
"""

q5="""the value of 5=8*3-8/4*7 is 
a)15
b)23
c)30
d)7.3
"""

questions={q1:"d",q2:"c",q3:"a",q4:"b",q5:"a"}
name=input("Hi Whats Your Name:")
print("Hello",name,"Welcome to the Quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip the question(yes/no):")
    if flag1=="yes":
        continue
    ans=input("Enter your answer:")
    if ans==questions[i]:
        print("wow ! you scored one point😍")
        score=score+1
        print("your score is ",score)
    else:
        print("you lose one point😢😒")
        score=score-1
        print("your score is ",score)
    flag2=("do you want to quit this quiz")
    if flag2=="yes":
        break
print("Your Total Score is ",score)