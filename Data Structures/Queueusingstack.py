n=int(input())
l1=[]
l2=[]
for i in range(n):
    l=input()
    l1.append(l)
for i in range(len(l1)):
    d=l1.pop()
    l2.append(d)
print(l2)
for i in range(len(l2)):
    print(l2.pop())
    
