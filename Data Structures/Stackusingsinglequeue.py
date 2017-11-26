from collections import deque
q1=deque()
n=int(input())
for i in range(n):
    d=input()
    q1.append(d)
n1=int(input("How many elements do u want to pop \n"))
for i in range(n1):
    for i in range(len(q1)-1):
        e=q1.popleft()
        q1.append(e)
    print(q1)
    print(q1.popleft())
        

