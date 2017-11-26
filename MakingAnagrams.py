#!/bin/python3

def makingAnagrams(s1, s2):
    checked=[]
    checked2=[]
    c=0
    s3=s2
    for i in s1:
        if i in s2:
            checked.append(i)
            s2=s2.replace(i,"",1)
            print(s2)
        else:
            c=c+1
    for i in s3:
        if i in s1:
            checked2.append(i)
            s1=s1.replace(i,"",1)
            print(s1)
        else:
            c=c+1
    return c

s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
