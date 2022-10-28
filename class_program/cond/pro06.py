wage = float (input("Enter your wage for your employ: "))
if wage <= 1250:
    new_wage = wage +(wage * 15 /100)
else:
    new_wage = wage + (wage * 10 /100)
print("your last salarie is {}RS now you want to receved {}RS".format(wage,new_wage))