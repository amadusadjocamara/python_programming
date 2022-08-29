num = int(input("Enter the vsluer of n: "))

a = num

sum = 0

if num <= 0:
    print("Enter a positve number: ")
else:
    while num > 0:
        sum = sum + num
        num = num - 1

print("Sum of frist" , a, " natural numbers is: ",sum)
        
