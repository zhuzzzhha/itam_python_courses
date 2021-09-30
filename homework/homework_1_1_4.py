a=input().split()
more_8=0
negative=0
even=0
for i in range(len(a)):
    if a[i]<0:
        negative+=1
    if a[i]>8:
        more_8+=1
    if a[i]%2==0:
        even+=1
print("больше 8 - ", more_8,"отрицательных - ", negative, "четных - ", even)
