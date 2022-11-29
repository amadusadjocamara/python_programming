n1 =int(input("frist segument: "))
n2 =int(input("second seguement: "))
n3 = int(input("thrid segurment: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 + n1 +n2:
    print(" you can create triable. ", end=" ")
    if n1 == n2 == n3:
        print("EQUILATERAL")
    elif n1 =! n2 =! n3 =! n1:
        print("SCALENE")
    else:
        print("ISOSCELES")
else:
    print("can not form triangle.")