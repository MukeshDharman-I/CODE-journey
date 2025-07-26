num=[1,45,6,4,2,7,8,9]
num=sorted(num)
s=45
l=0
r=len(num)-1
while l<=r:
    mid=(l+r)//2
    if num[mid]==s:
        print(mid)
        break
    elif num[mid]<s:
        l=mid+1
    elif num[mid]>s:
        r=mid-1
else:
    print(-1)