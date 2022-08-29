number = int (input ("Enter the number n:"))

a = number

sum = 0

if number <= 0:
    print("Enter the positive number.")
else:
    while number > 0:
        sum = sum + number 
        number = number -1
print("Sum of frist ", a," natural number is:", sum)
