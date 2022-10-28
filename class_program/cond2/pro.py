pre = float(input("Enter price house: "))
sal = float(input("what is your salary: "))
yer = int (input("when you want to pay: "))
print("="*50)
print()
prese = pre /(yer*12)
sml = sal *30/100
print("to pay one house {} for years {}".format(pre,yer) ,end = "")
print("valuer is {:2f} ".format(prese))
if prese <= sml:
    print("loa accetpted.")
else:
    print("loan not accepted")