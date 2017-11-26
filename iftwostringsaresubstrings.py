def isSubstring(s1,s2):
    if(len(s1)!=len(s2)):
        return "False"
    else:
        s1=s1.lower()
        s2=s2.lower()
        l1=list(s1)
        l2=list(s2)
        l1=l1.sort()
        l2=l2.sort()
        if(l1==l2):
            return "True"
        else:
            return "False"
        
    
s1=input("Enter the string 1")
s2=input("Enter the string 2")
c1=isSubstring(s1,s2)
print(c1)