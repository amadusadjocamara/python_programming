def add(a,b):
    return a + b
def mult(a,b):
    return a * b
def sub (a,b):
    return float (a) - float (b)
def div (a,b):
    return float (a) / float (b)

num1 = int(input("Ente you first number: "))
num2 = int (input("Enter your second number: "))
operat = input("Enter an opereator (+, -, *., /): ")

if operat == "+":
    print(f"The result is: {add(num1, num2)}")
elif operat == "*":
    print(f"The result is: {mult(num1, num2)}")
elif operat == "-":
    print(f"The result is: {sub(num1, num2)}")
elif operat == "/":
    print (f"The result is: {div(num1, num2)}")
else:
    print ("invalid option, please try againt.")
