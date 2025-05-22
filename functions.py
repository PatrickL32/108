#Functions
#Is a block of code which only runs when its called
#We can pass data, known as parameters and the function can data as a result.

#Simple functions witout parameters
def my_function():
    print("Hello from a function!")


def other_function():
    print ("this is  another function!")
#my_function()
#other_function()

def  print_full_name(fname,flast_name):
    print (f"{fname} {flast_name}")

#print_full_name(10,15)
#print_full_name(fname="Patrick", flast_name="Lewis")

def print_full_name_two(fname, flast_name):
    return f"{fname} {flast_name}"

#full_name = print_full_name_two("Patrick", "Lewis")
#print(full_name)

def add(x,y):
    return x+y

result = add(10,3)
print(result)

def subtract(a,b):
    return a-b

result=subtract(26,19)
print(result)

#input method
#is going to allow us to interact with the terminal and pass some values
name= input("Enter your name:")
print(name)

#age= input("Enter you age:")
#print(age)

#x=input("Enter a value:")
#print(type(x))
#y=input("Enter a second value:")
#print(type(y))
#print(x+y)

x=int(input("Enter a value:"))
print(type(x))
y=int(input("Enter a second value"))
print(type(y))
print(x+y)

print(add(x,y))





