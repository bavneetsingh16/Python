s=input("Enter the number to be checked")
d=int(s)
sum=0
for i in range(1,d):
    if(d%i == 0):
        sum=i+sum
if sum==d:
    print("perfect number")
