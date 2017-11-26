

def funnyString(s):
    s1=s[::-1]
    n=len(s)
    for i in range(1,n):
        a=ord(s[i])
        b=ord(s[i-1])
        c=ord(s1[i])
        d=ord(s1[i-1])
        if(abs(a-b) == abs(c-d)):
            temp=1;
        else:
            return "Not Funny"
    if(temp==1):
        return "Funny"
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)