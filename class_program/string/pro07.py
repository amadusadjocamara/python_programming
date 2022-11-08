from datetime import date
today = date.today().year
yer = int(input("Enter year: "))
old = today-yer
print(" who was brow in {} he have {} in this year {}".format(yer,old,today ))
if old ==18:
    print("you have to go to service.")
elif old < 18:
    print("its not time ")
elif old > 18:
    print("you should go to service {} years".format(old - 18))