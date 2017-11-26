from collections import deque
q1=deque()
q2=deque()
s=[]
temp=deque()
n=int(input())
for i in range(n):
    s=input()
    q2.append(s)
    while(len(q1) != 0):
        d=q1.popleft()
        q2.append(d)
    temp=q1
    q1=q2
    q2=temp
print(q1)
print(q1.pop())
    