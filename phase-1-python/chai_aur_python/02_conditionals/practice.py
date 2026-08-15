'''
#1 
age=int(input("enter you age : "))

if age < 13:
    print("you are child")
elif age>13 and age<19:
    print("teenage")
elif age > 20 and age<59:
    print("adult")

else:
    print("senior")

#2
day=input("enter day : ")
if age>18:
    ticket=12
else:
    ticket=8
if day=="wednesday":
    ticket-=2
print(ticket)

'''
#3
score=int(input("enter you score : "))

if score <=60:
    grade="f"
elif score<=69:
    grade="d"
elif score<=79:
    grade="c"
elif score<=89:
    grade="b"
else:
    grade="A"
print(f"your grade for {score} is {grade}")
