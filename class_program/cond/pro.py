import random
from time import sleep
num = random.randint(0,5)
print("Guess the number [0] to [5]")
gues = int(input())
print("lodin.....")
sleep(4)

if gues == num:
    print("good you win")
else:
    print("i win number is {}".format(num))
