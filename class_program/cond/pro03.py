sl = int(input("Enter the spet of car for: " ))
if sl > 80:
    print("you surpassed limet 80km\h")
    print("-=-"*10)
    print("You have to pay money. ")
    mn = (sl -80)* 7.00
    print("this amount {:2f}RS you have to pay".format(mn))
print("good! have good day")
