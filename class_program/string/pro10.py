from datetime import date
tod = date.today().year 
yer = int(input("Enter years you brond: "))
y = tod - yer
print("you have {} years.".format(y))
if y <= 9:
    print("Classification: Mirim")
elif y > 9 and y <= 14:
    print("Classification: childish")
elif y > 15 and y <= 19:
    print("Classification: Junior")
elif y > 20 and y  <= 25:
    print("Classification: senior")
else:
    print("classsification:master")  
