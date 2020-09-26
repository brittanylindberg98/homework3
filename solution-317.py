#nested loops

#a
print('(A)')
for i in range (0,10):
    for j in range (0,i+1):
        print("*", end = " ")
    print(" ")
print(" ")

#b
print('(B)')
for i in range (0,10):
    for j in range (0,10-i):
        print("*", end = " ")
    print(" ")
print(" ")

k =2*10-2
k =-1
#c
print('(c)')
k = -1
for i in range(10-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

#d
k = 2 * 10 - 2
print("(D)")
for i in range(0, 10):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
