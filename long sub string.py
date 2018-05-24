def rept(m):
    flag=0
    for x in range(len(m)):
        for y in range(x+1,len(m)):
            if m[x]==m[y]:
                flag=1
                break
    if flag==1:
        return -1
    else:
        return 0
    
st=input("Enter your string:")
s=list(st)
l=-1
for x in range(len(s)):
    for y in range(x+1,len(s)+1):
        ans=''
        for z in range(x,y):
            ans=ans+s[z]
        k=rept(ans)
        if k==0:
            if len(ans)>l:
                l=len(ans)
print(l)
© 2018 GitHub, Inc.
