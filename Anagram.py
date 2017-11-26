import sys

def anagram(s):
    s1=len(s)
    n1=int(s1/2)
    if(s1%2 != 0):
        return -1
    else:
        j=s[0:n1]
        k=s[n1:]
        c=0
        for l in j:
            if l not in k:
                c=c+1
            else:
                k=k.replace(l,"",1)
        return c            
                

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)