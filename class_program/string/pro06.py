yer = int(input("Enter your years: "))
if yer < 18:
    print("is not time to service. ")
elif yer == 18:
    print("is time to service.")
elif yer > 18 and yer ==30 :
    print("you have {} more".format(yer -18))
elif yer > 30:
    print("you can not register.")
