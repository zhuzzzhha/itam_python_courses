a=input().split()
mmax=a[0]
mmin=a[0]
for i in range(len(a)):
    if a[i]>mmax:
        mmax=a[i]
    if a[i]< mmin:
        mmin=a[i]
print("max=",mmax, "min=", mmin)
