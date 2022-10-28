name = str(input("Enter your name: ")).strip()
rool = int(input("Enter your rool N: "))
clas = str(input("Enter class: ")).strip()
if int(clas) >= 2020:
    print("Godd morning {}".format(name))
    print("="*50,"|")
    print("Enter please enter your marks:")
    ds_mar = float(input("Enter marks Dstruture: "))
    pyth = float(input("Enter marks python: "))
    netw = float(input("Enter marks for network: "))
    sum = ds_mar + pyth + netw 
    m = sum / 3
    if sum >= 19.0:
        print("very good: {}".format(name))
        print("your final media is {:2}".format(m))
    else:
        print("sorry you have to stude mor: {}".format(name))
else:
    print("wron year {} sorry".format(name))

