
def print_header(title):
    print("------------------------------------")
    print(title)
    print("------------------------------------")


def roll_call():
    names=["Patrick" ,"Ivan", "Ashlee", "Kenny"]
    print(names[0])
    print(names[1])
    print(names[2])
    print(names[3])
    print_header("loop 1")

    for student in names:
        print( student)



def get_total():
    print_header("   Prices")
    prices = [12, 56, 21, 6, 45, 47, 12, 9, 39, 74,8,3,15,99,60]
    total = 0
    for price in prices:
        print(price)
        total=total+price

    # when for loop finish.
    print_header(total)




def print_cheap_prices():
    print_header("   Cheap Prices")
    prices = [12, 56, 21, 6, 45, 47, 12, 9, 39, 74,8,3,15,99,60]
    for price in prices:
        if price < 50:
            print(price)


def print_expensive_prices(): # class mini challenge
    print_header("   Expensive prices")
    prices = [ 59, 77, 96, 85, 266, 72, 89, 100, 174,88,125,60]
    for price in prices:
        if price> 50:
            print(price)


def start_program():
    print_header("   Patrick") #call the function
    print(" Hello from loops")
    roll_call()
    get_total()
    print_cheap_prices()
    print_expensive_prices()





#when the program starts, we call
start_program()