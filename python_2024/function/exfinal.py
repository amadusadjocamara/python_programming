num1 = float(input("Enter your first number: "))
num2 =float (input("Enter you second number: "))
#The add function
def add( num1, num2):
    sum = int(num1) + int(num2)
    print(f"The Add {num1} + {num2} = {sum}")
#The subtract
def subt(num1, num2):
    subtr = float(num1) - float(num2)
    print(f"The subt {num1} - {num2} = {subtr}")
def mult(num1, num2):
    mul = int (num1) * int (num2)
    print(f"The mult {num1} * {num2} = {mul}")

add(num1, num2)
subt(num1, num2)
mult(num1, num2)