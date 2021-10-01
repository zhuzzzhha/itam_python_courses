och=0
zaoch=0
n=int(input())
for i in range(n):
    a=input().split()
    if a[3]=='True':
        och=och+1
    else:
        zaoch=zaoch+1
print(och,zaoch)
