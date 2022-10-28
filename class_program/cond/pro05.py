s1 = int(input("frist number: "))
s2 = int(input("Second number: "))
s3 = int(input("third number: "))
smll = s1

if s2<s1 and s2<s3:
    smll = s2
if s3 < s1 and s3 < s2:
    smll = s3

large = s1
if s2 > s1 and s2> s3:
    large = s2
if s3 > s1 and s3 > s2:
    large = s3
print("smaller number is {} ".format(smll))
print("large number is {} ".format(large))
