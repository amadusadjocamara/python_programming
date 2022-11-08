from time import sleep


num = int(input("Digiti number: "))
print("chose one number to converct.")
print("[1] to convert to binnary.")
print("[2] to convert to octal. ")
print("[3] to convert to hexd. ")
opc = int(input("Enter opction. "))
print("lodn...")
sleep(4)
if opc == 1:
    print("{} converct to binnaary is igual to {}".format(num,bin(num)))
elif opc == 2:
    print("{} converct to octal is igual to {}".format(num, oct(num)))
elif opc == 3:
    print("{} converct to hexd is igual to {} ".format(num,hex(num)))
else:
    print("erro")