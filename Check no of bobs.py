s="dasdasbobobsafdasfbobbob"
n=len(s)
j=0
for i in range(0,n):
    q=s[i]
    if i < n-1:
        if q == 'b':
            if s[i+1] == 'o' and s[i+2]=='b':
                j=j+1
print(j)
            
      