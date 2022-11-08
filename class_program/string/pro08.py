mar1 = float(input("Enter marks Ev:  "))
mar2 = float(input("Enter marks Python: "))
med = (mar1 + mar2) / 2
print("your fris marks is {} second marks {} your media is {}.".format(mar1,mar2,med))
if med >= 5 and med < 7 :
    print("student recovery. ")
elif med < 5:
    print("student failled.")
else:
    print("student pass. ")