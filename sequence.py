# Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___

# 3 seinustu tölur lagðar saman og mynda næstu tölu

n = int(input("Enter the length of the sequence: ")) # Do not change this line

n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = n3 + n2 + n1

for x in range(1, n + 1):
    if x <= 3:
        print(n0 + x)
    else:
        n4 = n1 + n2 + n3
        n1 = n2
        n2 = n3
        n3 = n4
        print(n4)