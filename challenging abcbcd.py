s=input("Enter the string \n")
n=len(s)
s1=s
c=0
s2=""
for i in range(n):
    if i<n-1 and (s1[i]<s1[i+1] or s1[i]>s1[i-1]):
        c=c+1
        s2=s2+s1[i]
    if i==n-1 and s1[i]>s1[i-1]:
        s2=s2+s1[i]
print(s2)