from math import ceil
n = int(input("Enter a posotive integer to factorise: "))
num = n
factors = []

p = 2
while n > 1:
    flag = False
    i = 2
    while i <= ceil(p/2) and flag == False:
        if p/i == int(p/i):
            flag = True
            p = p+1
        i = i+1
    if flag == False:
        #find a prime number and check if it factorises n
        while n % p == 0:
            factors.append(p)
            n = n/p
        p = p+1

if len(factors)==1:
    print(str(num)+" is prime")
else:
    print(str(num)+"="+str(factors))
