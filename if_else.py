print(3+2)
print(10-3)
print(5*3)
print(10/2)

x=10
y=3
print(x+y)
print(x*y)

age = 15
#if statements
#execute some instructions if the condition it's correct
#we can catch with on else in case that condition doesn't match
# equals: a==b
#Not Equals: a != b
#less than: a<b
#greater than:a>b
#less than or equal: a<=b
#greater than or equal:a>=b
if age < 100:
    if age > 21:
        print(f" you're a minor.")
    else:
        print(f"Don't worry you're super young!")
elif age == 100:
    print(f" Congradulations, you got to live a century!")
else:
    print(f"sorry, you're getting old!")

#exercise
x=5
y=8
if x>y:
    print("Hello")
elif x==10:
    print("world")
else:
    print("welcome")

x= "Hello"
y ="hello"

if x==y:
    print("Hey it's the same word.")
else:
    print("They're different!")